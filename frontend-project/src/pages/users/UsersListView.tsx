import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { User } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { UsersService } from '@/services/users';
import { openRemoveConfirmationModal } from '@/utils/utils';

export default function UsersListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.users;

  function onEdit(user: User) {
    router.push(`/users/edit/${user.id}`);
  }

  function onRemove(user: User) {
    openRemoveConfirmationModal(`${user.firstName} ${user.lastName} (${user.email})`, () =>
      UsersService.remove(user.id)
        .then(() => tableActionRef.current?.reload())
        .catch(() => tableActionRef.current?.reload()),
    );
  }

  const columns: ProColumns<User>[] = [
    {
      title: formatMessage({ id: fields.username }),
      dataIndex: ['username', 'id'],
      render: (_, record: User) => <Link to={`/users/edit/${record.id}`}>{record.username}</Link>,
    },
    {
      title: formatMessage({ id: fields.email }),
      dataIndex: 'email',
    },
    {
      title: formatMessage({ id: fields.firstName }),
      dataIndex: 'firstName',
    },
    {
      title: formatMessage({ id: fields.lastName }),
      dataIndex: 'lastName',
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, record: User) => (
        <Space>
          <Tooltip title={formatMessage({ id: localeKeys.lists.edit })}>
            <Button
              type="default"
              shape="circle"
              icon={<EditOutlined />}
              onClick={() => onEdit(record)}
            />
          </Tooltip>
          <Tooltip title={formatMessage({ id: localeKeys.lists.delete })}>
            <Button
              type="default"
              danger
              shape="circle"
              icon={<DeleteOutlined />}
              onClick={() => onRemove(record)}
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
      service={UsersService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
