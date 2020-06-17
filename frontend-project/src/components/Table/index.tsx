import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable, { ActionType, ProColumns } from '@ant-design/pro-table';
import React, { FC, useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { PaginationParams, PaginationResponse } from '@/services/common.d';

interface Table {
  type: string;
  columns: ProColumns<{}>[];
  fetchData: (parameter: PaginationParams) => Promise<PaginationResponse<{}>>;
}

const Table: FC<Table> = props => {
  const actionRef = useRef<ActionType>();

  const showTotal = (total: number, range: number[]) =>
    `${range[0]}-${range[1]} / ${formatMessage({ id: `${props.type}-list.table.total` })} ${total}`;

  return (
    <PageHeaderWrapper content={formatMessage({ id: `${props.type}-list.page-header-content` })}>
      <ProTable
        headerTitle={formatMessage({ id: `${props.type}-list.table-header-title` })}
        actionRef={actionRef}
        rowKey="id"
        tableAlertRender={false}
        request={props.fetchData}
        columns={props.columns}
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
