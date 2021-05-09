import { Spin } from 'antd';
import React, { useEffect, useState } from 'react';
import { Link } from 'umi';
import { formatMessage } from 'umi-plugin-react/locale';
import { localeKeys } from '../locales/pl-PL';
import { openNotificationWithIcon } from '../models/global';
import { AutocompleteFunctionType, AutocompleteServiceType } from '../services/autocomplete';
import { Awaited, KeysWithValsOfType } from '../services/common';
import { ResourceWithId } from '../services/service';
import { QQ } from '../utils/QQ';

export function FetchLink<
  T extends Awaited<ReturnType<AutocompleteServiceType[keyof AutocompleteServiceType]>>[number] & {
    name?: string;
  },
  SearchField extends (string & KeysWithValsOfType<T, string>) | 'name'
>({
  route,
  id,
  autocompleteFunction,
  labelField,
}: {
  route: keyof AutocompleteServiceType;
  id: ResourceWithId['id'] | null;
  autocompleteFunction: AutocompleteFunctionType<T>;
  labelField?: SearchField;
}) {
  const [isFetching, setFetching] = useState(true);
  const [label, setLabel] = useState<string>('');
  const searchField = labelField || 'name';
  const onError = () => {
    openNotificationWithIcon(
      'error',
      formatMessage({ id: localeKeys.error }),
      formatMessage({ id: localeKeys.autocompleteError }),
    );
  };

  useEffect(() => {
    if (!id) return;
    autocompleteFunction({
      query: QQ.field('id', id),
      pageSize: 10,
    })
      .then(autocompleteResults => {
        setLabel((autocompleteResults?.[0][searchField] as string) || '');
      })
      .catch(onError)
      .finally(() => setFetching(false));
  }, []);

  if (!id) {
    return null;
  }
  return isFetching ? <Spin size="small" /> : <Link to={`/${route}/edit/${id}/`}>{label}</Link>;
}
