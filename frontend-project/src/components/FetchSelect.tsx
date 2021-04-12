import { localeKeys } from '@/locales/pl-PL';
import { Select, Spin } from 'antd';
import { SelectProps } from 'antd/es/select';
import React, { useEffect, useState } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { useDebounce } from '../hooks/useDebounce';
import { openNotificationWithIcon } from '../models/global';
import { AutocompleteFunctionType, AutocompleteServiceType } from '../services/autocomplete';
import { Awaited, KeysWithValsOfType, OptionType } from '../services/common';
import { QQ } from '../utils/QQ';

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
    if (
      typeof value === 'undefined' ||
      value === null ||
      arrayValue.length === 0 ||
      mode === 'tags'
    )
      return;
    setShownOptions([]);
    setFetching(true);

    autocompleteFunction({
      query: QQ.in('id', arrayValue),
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
        query: QQ.icontains(searchField, search),
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
