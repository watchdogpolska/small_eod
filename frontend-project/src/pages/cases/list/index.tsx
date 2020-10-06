import { ProColumns } from '@ant-design/pro-table';
import { Tag } from 'antd';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Case, fetchCasesPage } from '@/services/cases';
import Table from '@/components/Table';
import InstitutionName from '@/components/Table/InstitutionName';

const TableList: FC<{}> = () => {
  const columns: ProColumns<Case>[] = [
    {
      title: formatMessage({ id: 'cases-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.audited_institutions.title' }),
      dataIndex: 'auditedInstitutions',
      render: (auditedInstitutions: number[]) => (
        <>
          {auditedInstitutions.map(auditedInstitution => (
            <InstitutionName id={auditedInstitution} key={auditedInstitution} />
          ))}
        </>
      ),
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.comment.title' }),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.createdOn.title' }),
      dataIndex: 'createdOn',
      render: createdOn => createdOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.modifiedOn.title' }),
      dataIndex: 'modifiedOn',
      render: modifiedOn => modifiedOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.tags.title' }),
      dataIndex: 'tags',
      render: (tags: number[]) => (
        <>
          {tags.map(tag => (
            <Tag color="blue" key={tag}>
              {tag}
            </Tag>
          ))}
        </>
      ),
    },
    {
      title: formatMessage({ id: 'cases-list.table.columns.letterCount.title' }),
      dataIndex: 'letterCount',
    },
  ];
  return <Table type="cases" columns={columns} fetchData={fetchCasesPage} />;
};

export default TableList;
