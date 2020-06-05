import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Case, fetchCasesPage } from '@/services/cases';
import Table from '@/components/Table';

const TableList: FC<{}> = () => {
  const columns: ProColumns<Case>[] = [
    {
      title: formatMessage({ id: 'cases-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.audited_institutions.title' }),
      dataIndex: 'auditedInstitutions',
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.comment.title' }),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.createdOn.title' }),
      dataIndex: 'createdOn',
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.modifiedOn.title' }),
      dataIndex: 'modifiedOn',
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.tags.title' }),
      dataIndex: 'tags',
    },
  ];
  return <Table type="cases" columns={columns} fetchData={fetchCasesPage} />;
};

export default TableList;
