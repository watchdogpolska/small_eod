import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import Table from '@/components/Table';
import { Feature } from '@/services/definitions';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { localeKeys } from '@/locales/pl-PL';
import { openNotificationWithIcon } from '@/models/global';
import { FeaturesService } from '@/services/features';

const TableList: FC<{}> = () => {
  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<Feature>> {
    const response = await FeaturesService.fetchPage(props);
    if (response.status === 'failed') {
      openNotificationWithIcon(
        'error',
        formatMessage({ id: localeKeys.error }),
        formatMessage({ id: localeKeys.lists.failedDownload }),
      );
      return { data: [], total: 0 };
    }
    return response.data;
  }

  const columns: ProColumns<Feature>[] = [
    {
      title: formatMessage({ id: 'features-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
    {
      title: formatMessage({ id: 'features-list.table.columns.minOptions.title' }),
      dataIndex: 'minOptions',
    },
    {
      title: formatMessage({ id: 'features-list.table.columns.maxOptions.title' }),
      dataIndex: 'maxOptions',
    },
  ];

  return <Table type="features" columns={columns} fetchData={fetchPage} />;
};

export default TableList;
