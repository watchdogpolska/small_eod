import { ProColumns } from '@ant-design/pro-table';
import { Tag } from 'antd';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import Table from '@/components/Table';
import { Institution, fetchInstitutionPage } from '@/services/institutions';

const TableList: FC<{}> = () => {
  const columns: ProColumns<Institution>[] = [
    {
      title: formatMessage({ id: 'institutions-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
    {
      title: formatMessage({ id: 'institutions-list.table.columns.comment.title' }),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({ id: 'institutions-list.table.columns.createdOn.title' }),
      dataIndex: 'createdOn',
      render: createdOn => createdOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'institutions-list.table.columns.modifiedOn.title' }),
      dataIndex: 'modifiedOn',
      render: (modifiedOn: string) => modifiedOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'institutions-list.table.columns.tags.title' }),
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
  ];

  return <Table type="institutions" columns={columns} fetchData={fetchInstitutionPage} />;
};

export default TableList;
