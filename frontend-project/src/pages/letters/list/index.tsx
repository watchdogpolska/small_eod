import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable, { ProColumns, ActionType } from '@ant-design/pro-table';
import React, { FC, useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Letter, fetchLettersPage } from '@/services/letters';
import { CaseName } from '@/components/Table/CaseName';
import { InstitutionName } from '@/components/Table/InstitutionName';

const TableList: FC<{}> = () => {
  const actionRef = useRef<ActionType>();
  const columns: ProColumns<Letter>[] = [
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
      render: (direction: string) =>
        formatMessage({ id: `letters-list.table.direction.${direction.toLowerCase()}` }),
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.case.title' }),
      dataIndex: 'case',
      render: (_case: number) => (typeof _case === 'number' ? <CaseName id={_case} /> : _case),
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.audited_institutions.title' }),
      dataIndex: 'institution',
      render: (institution: number) => <InstitutionName id={institution} />,
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.createdOn.title' }),
      dataIndex: 'createdOn',
      render: createdOn => createdOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.modifiedOn.title' }),
      dataIndex: 'modifiedOn',
      render: modifiedOn => modifiedOn.toLocaleString(),
    },
  ];

  const showTotal = (total, range) =>
    `${range[0]}-${range[1]} / ${formatMessage({ id: 'letters-list.table.total' })} ${total}`;

  return (
    <PageHeaderWrapper content={formatMessage({ id: 'letters-list.page-header-content' })}>
      <ProTable<Letter>
        headerTitle={formatMessage({ id: 'letters-list.table-header-title' })}
        actionRef={actionRef}
        rowKey="id"
        tableAlertRender={false}
        request={fetchLettersPage}
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
