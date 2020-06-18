import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Letter, fetchLettersPage } from '@/services/letters';
import Table from '@/components/Table';

const TableList: FC<{}> = () => {
  const columns: ProColumns<Letter>[] = [
    {
      title: formatMessage({ id: 'letters-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.identifier.title' }),
      dataIndex: 'identifier',
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.comment.title' }),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.direction.title' }),
      dataIndex: 'direction',
    },
  ];

  return <Table type="letters" columns={columns} fetchData={fetchLettersPage} />;
};

export default TableList;
