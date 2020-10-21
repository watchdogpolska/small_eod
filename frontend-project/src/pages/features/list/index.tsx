import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import Table from '@/components/Table';
import { fetchFeaturesPage } from '@/services/features';
import { Feature } from '@/services/definitions';

const TableList: FC<{}> = () => {
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

  return <Table type="features" columns={columns} fetchData={fetchFeaturesPage} />;
};

export default TableList;
