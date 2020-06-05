import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable, { ProColumns, ActionType } from '@ant-design/pro-table';
import React, { FC, useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Case, fetchCasesPage } from '@/services/cases';

const TableList: FC<{}> = () => {
  const actionRef = useRef<ActionType>();
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

  const showTotal = (total, range) =>
    `${range[0]}-${range[1]} / ${formatMessage({ id: 'cases-list.table.total' })} ${total}`;

  return (
    <PageHeaderWrapper content={formatMessage({ id: 'cases-list.page-header-content' })}>
      <ProTable<Case>
        headerTitle={formatMessage({ id: 'cases-list.table-header-title' })}
        actionRef={actionRef}
        rowKey="id"
        tableAlertRender={false}
        request={fetchCasesPage}
        columns={columns}
        rowSelection={false}
        search={false}
        options={false}
        pagination={{
          pageSize: 20,
          showSizeChanger: false,
          showTotal,
        }}
      />
    </PageHeaderWrapper>
  );
};

export default TableList;
