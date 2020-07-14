import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { User, fetchUsersPage } from '@/services/users';
import Table from '@/components/Table';

const TableList: FC<{}> = () => {
  const columns: ProColumns<User>[] = [
    {
      title: formatMessage({ id: 'users-list.table.columns.username.title' }),
      dataIndex: 'username',
    },
    {
      title: formatMessage({ id: 'users-list.table.columns.email.title' }),
      dataIndex: 'email',
    },
    {
      title: formatMessage({ id: 'users-list.table.columns.firstName.title' }),
      dataIndex: 'firstName',
    },
    {
      title: formatMessage({ id: 'users-list.table.columns.lastName.title' }),
      dataIndex: 'lastName',
    },
  ];

  return <Table type="users" columns={columns} fetchData={fetchUsersPage} />;
};

export default TableList;
