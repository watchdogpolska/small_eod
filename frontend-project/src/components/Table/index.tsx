import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable, { ActionType, ProColumns } from '@ant-design/pro-table';
import React, { MutableRefObject } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { PaginationParams, PaginationResponse } from '@/services/common.d';
import { localeKeys } from '../../locales/pl-PL';

interface TableProps<T> {
  type: string;
  columns: ProColumns<T>[];
  fetchData: (parameter: PaginationParams) => Promise<PaginationResponse<T>>;
  pageHeader?: string;
  tableHeader?: string;
  actionRef?: MutableRefObject<ActionType>;
}

function Table<T>({ type, columns, fetchData, pageHeader, tableHeader, actionRef }: TableProps<T>) {
  const showTotal = (total: number, range: number[]) =>
    `${range[0]}-${range[1]} / ${formatMessage({ id: localeKeys.lists.total })} ${total}`;

  return (
    <PageHeaderWrapper
      content={formatMessage({ id: pageHeader || `${type}-list.page-header-content` })}
    >
      <ProTable
        headerTitle={formatMessage({ id: tableHeader || `${type}-list.table-header-title` })}
        actionRef={actionRef}
        rowKey="id"
        request={fetchData}
        tableAlertRender={false}
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
}

export default Table;
