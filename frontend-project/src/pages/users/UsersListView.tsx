import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { User } from '@/services/definitions';
import { UsersService } from '@/services/users';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { useDispatch } from 'dva';
import { Link } from 'umi';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { openNotificationWithIcon } from '@/models/global';
import { ServiceResponse } from '@/services/service';
import { localeKeys } from '@/locales/pl-PL';

function UsersListView() {
  const dispatch = useDispatch();
  const tableActionRef = useRef<ActionType>();

  function onEdit(id: number) {
    router.push(`/users/edit/${id}`);
  }

  function onRemove(id: number) {
    dispatch({
      type: 'users/remove',
      payload: {
        id,
        onResponse: (response: ServiceResponse<number>) => {
          if (response.status === 'failed') {
            openNotificationWithIcon(
              'error',
              formatMessage({ id: localeKeys.error }),
              `${formatMessage({ id: localeKeys.cases.list.failedRemove })} ${id}`,
            );
          }
          tableActionRef.current?.reload();
        },
      },
    });
  }

  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<User>> {
    const response = await UsersService.fetchPage(props);
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

  const columns: ProColumns<User>[] = [
    {
      title: formatMessage({ id: localeKeys.users.fields.username }),
      dataIndex: ['username', 'id'],
      render: (_, record: User) => <Link to={`/users/edit/${record.id}`}>{record.username}</Link>,
    },
    {
      title: formatMessage({ id: localeKeys.users.fields.email }),
      dataIndex: 'email',
    },
    {
      title: formatMessage({ id: localeKeys.users.fields.firstName }),
      dataIndex: 'firstName',
    },
    {
      title: formatMessage({ id: localeKeys.users.fields.lastName }),
      dataIndex: 'lastName',
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (id: number) => (
        <Space>
          <Tooltip title={formatMessage({ id: localeKeys.lists.edit })}>
            <Button
              type="default"
              shape="circle"
              icon={<EditOutlined />}
              onClick={() => onEdit(id)}
            />
          </Tooltip>
          <Tooltip title={formatMessage({ id: localeKeys.lists.delete })}>
            <Button
              type="default"
              danger
              shape="circle"
              icon={<DeleteOutlined />}
              onClick={() => onRemove(id)}
            />
          </Tooltip>
        </Space>
      ),
    },
  ];
  return (
    <Table
      type="users"
      columns={columns}
      fetchData={fetchPage}
      pageHeader={localeKeys.users.list.pageHeaderContent}
      tableHeader={localeKeys.users.list.table.header}
      actionRef={tableActionRef}
    />
  );
}

export default UsersListView;
