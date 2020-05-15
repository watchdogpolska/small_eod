import React, { useRef } from 'react';
import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable, { ProColumns, ActionType } from '@ant-design/pro-table';
import { formatMessage } from 'umi-plugin-react/locale';

import smallEodSDK from '@/utils/sdk';


export interface TableListItem {
  id: number;
  name: string,
  identifier: string,
  direction: string,
}

export interface TableListParams {
  pageSize: number;
  current: number;
}

export async function queryLetters(params?: TableListParams) {
  smallEodSDK.LettersApi();

  return smallEodSDK.lettersList({
    limit: params.pageSize,
    offset: params.pageSize * (params.current - 1),
  }).then((result) => ({
    data: result.results,
    total: result.count,
  }));
}

const TableList: React.FC<{}> = () => {
  const actionRef = useRef<ActionType>();
  const columns: ProColumns<TableListItem>[] = [
    {
      title: formatMessage({id: 'letters-list.table.columns.name.title'}),
      dataIndex: 'name',
    },
    {
      title: formatMessage({id: 'letters-list.table.columns.identifier.title'}),
      dataIndex: 'identifier',
    },
    {
      title: formatMessage({id: 'letters-list.table.columns.comment.title'}),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({id: 'letters-list.table.columns.direction.title'}),
      dataIndex: 'direction',
    },
  ];

  return (
    <PageHeaderWrapper content={formatMessage({ id: 'letters-list.page-header-content' })}>
      <ProTable<TableListItem>
        headerTitle={formatMessage({ id: 'letters-list.table-header-title' })}
        actionRef={actionRef}
        rowKey="id"
        tableAlertRender={false}
        request={queryLetters}
        columns={columns}
        rowSelection={false}
        search={false}
        options={false}
        pagination={{pageSize: 20, showSizeChanger: false, showTotal: (total, range) => `${range[0]}-${range[1]} / ${formatMessage({id: 'letters-list.table.total'})} ${total}`}}
      />
    </PageHeaderWrapper>
  );
};

export default TableList;
