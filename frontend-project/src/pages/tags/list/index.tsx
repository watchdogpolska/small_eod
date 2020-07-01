import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Tag, fetchTagsPage } from '@/services/tags';
import Table from '@/components/Table';

const TableList: FC<{}> = () => {
  const columns: ProColumns<Tag>[] = [
    {
      title: formatMessage({ id: 'tags-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
  ];
  return <Table type="tags" columns={columns} fetchData={fetchTagsPage} />;
};

export default TableList;
