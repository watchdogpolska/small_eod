import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { CheckCircleTwoTone, CloseCircleTwoTone } from '@ant-design/icons';

import { Channel, fetchChannelsPage } from '@/services/channels';
import Table from '@/components/Table';

const TableList: FC<{}> = () => {
  const columns: ProColumns<Channel>[] = [
    {
      title: formatMessage({ id: 'channels-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.email.title' }),
      dataIndex: 'email',
      render: email =>
        email ? (
          <CheckCircleTwoTone twoToneColor="#52C41A" />
        ) : (
          <CloseCircleTwoTone twoToneColor="#EB2F96" />
        ),
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.epuap.title' }),
      dataIndex: 'epuap',
      render: epuap =>
        epuap ? (
          <CheckCircleTwoTone twoToneColor="#52C41A" />
        ) : (
          <CloseCircleTwoTone twoToneColor="#EB2F96" />
        ),
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.city.title' }),
      dataIndex: 'city',
      render: city =>
        city ? (
          <CheckCircleTwoTone twoToneColor="#52C41A" />
        ) : (
          <CloseCircleTwoTone twoToneColor="#EB2F96" />
        ),
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.street.title' }),
      dataIndex: 'street',
      render: street =>
        street ? (
          <CheckCircleTwoTone twoToneColor="#52C41A" />
        ) : (
          <CloseCircleTwoTone twoToneColor="#EB2F96" />
        ),
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.houseNo.title' }),
      dataIndex: 'houseNo',
      render: houseNo =>
        houseNo ? (
          <CheckCircleTwoTone twoToneColor="#52C41A" />
        ) : (
          <CloseCircleTwoTone twoToneColor="#EB2F96" />
        ),
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.flatNo.title' }),
      dataIndex: 'flatNo',
      render: flatNo =>
        flatNo ? (
          <CheckCircleTwoTone twoToneColor="#52C41A" />
        ) : (
          <CloseCircleTwoTone twoToneColor="#EB2F96" />
        ),
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.postalCode.title' }),
      dataIndex: 'postalCode',
      render: postalCode =>
        postalCode ? (
          <CheckCircleTwoTone twoToneColor="#52C41A" />
        ) : (
          <CloseCircleTwoTone twoToneColor="#EB2F96" />
        ),
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.voivodeship.title' }),
      dataIndex: 'voivodeship',
      render: voivodeship =>
        voivodeship ? (
          <CheckCircleTwoTone twoToneColor="#52C41A" />
        ) : (
          <CloseCircleTwoTone twoToneColor="#EB2F96" />
        ),
    },
  ];

  return <Table type="channels" columns={columns} fetchData={fetchChannelsPage} />;
};

export default TableList;
