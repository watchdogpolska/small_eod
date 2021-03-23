import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable, { ActionType, ProColumns } from '@ant-design/pro-table';
import React, { MutableRefObject } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { localeKeys } from '../../locales/pl-PL';
import { PaginationParams } from '../../services/common';
import { ReadOnlyServiceType, ResourceWithId } from '../../services/service';

interface TableProps<TList extends ResourceWithId, TDetail extends ResourceWithId = TList> {
  type: string;
  columns: ProColumns<TList>[];
  service: ReadOnlyServiceType<TList, TDetail>;
  pageHeader?: string;
  tableHeader?: string;
  actionRef?: MutableRefObject<ActionType>;
}

function Table<TList extends ResourceWithId, TDetail extends ResourceWithId = TList>({
  type,
  columns,
  service,
  pageHeader,
  tableHeader,
  actionRef,
}: TableProps<TList, TDetail>) {
  const showTotal = (total: number, range: number[]) =>
    `${range[0]}-${range[1]} / ${formatMessage({ id: localeKeys.lists.total })} ${total}`;

  function fetchFromService(props: PaginationParams) {
    return service.fetchPage(props);
  }

  return (
    <PageHeaderWrapper
      content={formatMessage({ id: pageHeader || `${type}-list.page-header-content` })}
    >
      <ProTable
        headerTitle={formatMessage({ id: tableHeader || `${type}-list.table-header-title` })}
        actionRef={actionRef}
        rowKey="id"
        request={fetchFromService}
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
