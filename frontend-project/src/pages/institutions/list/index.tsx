import { ProColumns } from '@ant-design/pro-table';
import { Tag } from 'antd';
import React, { FC } from 'react';
import { formatMessage } from 'umi';

import Table from '@/components/Table';
import { localeKeys } from '@/locales/pl-PL';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { openNotificationWithIcon } from '@/models/global';
import { Institution } from '@/services/definitions';
import { InstitutionsService } from '@/services/institutions';

const TableList: FC<{}> = () => {
  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<Institution>> {
    const response = await InstitutionsService.fetchPage(props);
    if (response.status === 'failed') {
      openNotificationWithIcon(
        'error',
        formatMessage({ id: localeKeys.error }),
        formatMessage({ id: localeKeys.lists.failedDownload }),
      );
      return { data: [], total: 0 };
    }
    return response.data;
  }

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

  return <Table type="institutions" columns={columns} fetchData={fetchPage} />;
};

export default TableList;
