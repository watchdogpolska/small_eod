import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { connect } from 'dva';
import { formatMessage } from 'umi-plugin-react/locale';
import { CheckCircleTwoTone, CloseCircleTwoTone } from '@ant-design/icons';

import { Channel } from '@/services/channels';
import Table from '@/components/Table';
import { PaginationParams, PaginationResponse } from '@/services/common.d';

export interface IconProps {
  arg: boolean;
}

const Icon: FC<IconProps> = ({ arg }) =>
  arg ? (
    <CheckCircleTwoTone twoToneColor="#52C41A" />
  ) : (
    <CloseCircleTwoTone twoToneColor="#EB2F96" />
  );

const TableList: FC<{ dispatch: Function }> = ({ dispatch }) => {
  const fetchData = (parameter: PaginationParams): Promise<PaginationResponse<{}>> => {
    return dispatch({ type: 'channels/fetchPage', payload: parameter });
  };
  const columns: ProColumns<Channel>[] = [
    {
      title: formatMessage({ id: 'channels-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.email.title' }),
      dataIndex: 'email',
      render: (email: boolean) => <Icon arg={email} />,
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.epuap.title' }),
      dataIndex: 'epuap',
      render: (epuap: boolean) => <Icon arg={epuap} />,
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.city.title' }),
      dataIndex: 'city',
      render: (city: boolean) => <Icon arg={city} />,
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.street.title' }),
      dataIndex: 'street',
      render: (street: boolean) => <Icon arg={street} />,
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.houseNo.title' }),
      dataIndex: 'houseNo',
      render: (houseNo: boolean) => <Icon arg={houseNo} />,
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.flatNo.title' }),
      dataIndex: 'flatNo',
      render: (flatNo: boolean) => <Icon arg={flatNo} />,
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.postalCode.title' }),
      dataIndex: 'postalCode',
      render: (postalCode: boolean) => <Icon arg={postalCode} />,
    },
    {
      title: formatMessage({ id: 'channels-list.table.columns.voivodeship.title' }),
      dataIndex: 'voivodeship',
      render: (voivodeship: boolean) => <Icon arg={voivodeship} />,
    },
  ];

  return <Table type="channels" columns={columns} fetchData={fetchData} />;
};

export default connect()(TableList);
