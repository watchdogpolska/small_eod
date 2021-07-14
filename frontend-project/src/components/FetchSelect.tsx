import { localeKeys } from '@/locales/pl-PL';
import { Select, Spin } from 'antd';
import { SelectProps } from 'antd/es/select';
import React, { useEffect, useState } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { unionBy, sortBy } from 'lodash';
import { useDebounce } from '../hooks/useDebounce';
import { openNotificationWithIcon } from '../models/global';
import { AutocompleteFunctionType, AutocompleteServiceType } from '../services/autocomplete';
import { Awaited, KeysWithValsOfType, OptionType } from '../services/common';
import { QQ } from '../utils/QQ';

/**
 * Select field with autocompletion.
 *
 * Whenever a user types into the search field, the component will communicate with the backend
 * to show items matching the input.
 */
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

  function extractOptionsFromApiResults(results: T[]) {
    return results.map(
      result =>
        ({
          label: result[searchField] as string,
          value: mode === 'tags' ? result[searchField] : result.id,
        } as OptionsType),
    );
  }

  // Call the autocomplete api once to convert field ids, fetched from the object's detail endpoint,
  // into human readable names.
  // Uses the autocomplete API for (id => name) mapping for consistency - subsequent calls, triggered
  // by user input, will receive (id, name) pairs from the same API.
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
        setShownOptions(extractOptionsFromApiResults(autocompleteResults));
      })
      .catch(onError)
      .finally(() => setFetching(false));
  }, []);

  // Fetch (id, name) pairs matching the search string.
  // Invoked on every keystroke, after a short delay.
  const debounceFetcher = (search: string) => {
    if (!search) return [];
    setAutocompleteOptions([]);
    setFetching(true);

    return debouncePromise(() =>
      autocompleteFunction({
        query: QQ.icontains(searchField, search),
        pageSize: 10,
      })
        .then(autocompleteResults => {
          setAutocompleteOptions(extractOptionsFromApiResults(autocompleteResults));
        })
        .catch(onError)
        .finally(() => setFetching(false)),
    );
  };

  // All options to display to the user.
  // Sets may overlap - remove duplicates to avoid duplicate rendering issues.
  const options = sortBy(unionBy(shownOptions, autocompleteOptions, 'value'), 'label');

  return (
    <Select<OptionsType>
      showSearch
      mode={mode}
      filterOption={false}
      onSearch={debounceFetcher}
      notFoundContent={isFetching ? <Spin size="small" /> : null}
      {...props}
      options={options}
      value={value}
    />
  );
}
