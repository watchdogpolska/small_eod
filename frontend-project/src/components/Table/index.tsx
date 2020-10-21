import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable, { ActionType, ProColumns } from '@ant-design/pro-table';
import React, { FC, useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { PaginationParams, PaginationResponse } from '@/services/common.d';

interface TableProps {
  type: string;
  columns: ProColumns<{}>[];
  fetchData: (parameter: PaginationParams) => Promise<PaginationResponse<{}>>;
}

const Table: FC<TableProps> = ({ type, columns, fetchData }) => {
  const actionRef = useRef<ActionType>();

  const showTotal = (total: number, range: number[]) =>
    `${range[0]}-${range[1]} / ${formatMessage({ id: `${type}-list.table.total` })} ${total}`;

  return (
    <PageHeaderWrapper content={formatMessage({ id: `${type}-list.page-header-content` })}>
      <ProTable
        headerTitle={formatMessage({ id: `${type}-list.table-header-title` })}
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
};

export default Table;
