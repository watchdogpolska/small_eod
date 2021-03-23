import React, { useEffect, useState } from 'react';
import { Select, Spin } from 'antd';
import { SelectProps } from 'antd/es/select';
import { useDebounce } from '../hooks/useDebounce';
import { KeysWithValsOfType, OptionType } from '../services/common';
import { AutocompleteServiceType, AutocompleteFunctionType } from '../services/autocomplete';
import { QQ } from '../utils/QQ';
import { localeKeys } from '@/locales/pl-PL';
import { openNotificationWithIcon } from '@/models/global';
import { formatMessage } from 'umi-plugin-react/locale';

type Awaited<T> = T extends PromiseLike<infer U> ? Awaited<U> : T;

export function FetchSelect<
  Mode extends 'multiple' | 'tags' | undefined,
  OptionsType extends OptionType<string, Mode extends 'tags' ? string : number>,
  T extends Awaited<ReturnType<AutocompleteServiceType[keyof AutocompleteServiceType]>>[number] & {
    name?: string;
  },
  SearchField extends (string & KeysWithValsOfType<T, string>) | 'name',
  ValueType extends Mode extends 'tags' ? string[] : Mode extends 'multiple' ? number[] : number
>({
  mode,
  autocompleteFunction,
  labelField,
  value,
  ...props
}: Omit<SelectProps<OptionsType>, 'options' | 'children'> & {
  mode: Mode;
  autocompleteFunction: AutocompleteFunctionType<T>;
  value?: ValueType;
  labelField?: SearchField;
}) {
  const [isFetching, setFetching] = useState(false);
  const [shownOptions, setShownOptions] = useState<OptionsType[]>([]);
  const [autocompleteOptions, setAutocompleteOptions] = useState<OptionsType[]>([]);
  const { debouncePromise } = useDebounce();
  const searchField = labelField || 'name';
  const onError = () => {
    openNotificationWithIcon(
      'error',
      formatMessage({ id: localeKeys.error }),
      formatMessage({ id: localeKeys.autocompleteError }),
    );
  };

  useEffect(() => {
    const arrayValue = Array.isArray(value) ? value : [value];
    if (arrayValue.length === 0 || mode === 'tags') return;
    setShownOptions([]);
    setFetching(true);

    autocompleteFunction({
      ...QQ.in('id', arrayValue),
      pageSize: 10,
    })
      .then(autocompleteResults => {
        setShownOptions(
          autocompleteResults.map(
            result =>
              ({
                label: result[searchField] as string,
                value: mode === 'tags' ? result[searchField] : result.id,
              } as OptionsType),
          ),
        );
        setFetching(false);
      })
      .catch(onError);
  }, []);

  const debounceFetcher = (search: string) => {
    setAutocompleteOptions([]);
    setFetching(true);

    debouncePromise(() =>
      autocompleteFunction({
        ...QQ.icontains(searchField, search),
        pageSize: 10,
      })
        .then(autocompleteResults => {
          setAutocompleteOptions(
            autocompleteResults.map(
              result =>
                ({
                  label: result[searchField] as string,
                  value: mode === 'tags' ? result[searchField] : result.id,
                } as OptionsType),
            ),
          );
          setFetching(false);
        })
        .catch(onError),
    );
  };

  return (
    <Select<OptionsType>
      showSearch
      mode={mode}
      filterOption={false}
      onSearch={debounceFetcher}
      notFoundContent={isFetching ? <Spin size="small" /> : null}
      {...props}
      options={[...shownOptions, ...autocompleteOptions]}
      value={value}
    />
  );
}
