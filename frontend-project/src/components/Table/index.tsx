import { QQ } from '@/utils/QQ';
import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable, { ActionType, ProColumns } from '@ant-design/pro-table';
import { Input, Row, Col } from 'antd';
import { ExpandableConfig } from 'antd/lib/table/interface';
import React, { MutableRefObject, useRef, useState } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { localeKeys } from '../../locales/pl-PL';
import { PaginationParams } from '../../services/common';
import { ReadOnlyServiceType, ResourceWithId } from '../../services/service';

const { Search } = Input;

interface TableProps<T extends ResourceWithId> {
  type: string;
  columns: ProColumns<T>[];
  service: ReadOnlyServiceType<T>;
  pageHeader?: string;
  tableHeader?: string;
  actionRef?: MutableRefObject<ActionType>;
  expandable?: ExpandableConfig<T>;
  disableFilter?: boolean;
  filters?: { [key: string]: any };
  inline?: boolean;
}

function Table<T extends ResourceWithId>({
  type,
  columns,
  service,
  pageHeader,
  tableHeader,
  actionRef,
  expandable,
  disableFilter,
  filters,
  inline,
}: TableProps<T>) {
  const localActionRef = useRef<ActionType>();
  const usedActionRef = actionRef || localActionRef;

  const [filter, setFilter] = useState<string>('');
  const showTotal = (total: number, range: number[]) =>
    `${range[0]}-${range[1]} / ${formatMessage({ id: localeKeys.lists.total })} ${total}`;

  function fetchFromService(props: PaginationParams) {
    return service.fetchPage({
      ...props,
      query: QQ.and(
        props.query,
        QQ.and(
          filter,
          filters &&
            Object.entries(filters).reduce(
              (acc, [field, value]) => QQ.and(acc, QQ.field(field, value)),
              '',
            ),
        ),
      ),
    });
  }

  const PageHeader = inline
    ? ({ children }) => <>{children}</>
    : ({ children }) => (
        <PageHeaderWrapper
          content={formatMessage({ id: pageHeader || `${type}-list.page-header-content` })}
        >
          {children}
        </PageHeaderWrapper>
      );

  return (
    <PageHeader>
      <Row gutter={[16, 16]}>
        {!disableFilter && !inline && (
          <Col span={24} className="gutter-row">
            <Search
              placeholder={formatMessage({ id: localeKeys.lists.filters })}
              onSearch={value => {
                setFilter(value);
                usedActionRef.current.reload();
              }}
              enterButton
            />
          </Col>
        )}

        <Col span={24} className="gutter-row">
          <ProTable
            headerTitle={
              inline
                ? undefined
                : formatMessage({ id: tableHeader || `${type}-list.table-header-title` })
            }
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
            expandable={expandable}
          />
        </Col>
      </Row>
    </PageHeader>
  );
}

export default Table;
