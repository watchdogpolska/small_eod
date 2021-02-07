import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef, FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import {
  CheckCircleTwoTone,
  CloseCircleTwoTone,
  DeleteOutlined,
  EditOutlined,
} from '@ant-design/icons';

import { Channel } from '@/services/definitions';
import { ChannelsService } from '@/services/channels';
import Table from '@/components/Table';
import router from 'umi/router';
import { useDispatch } from 'dva';
import { Link } from 'umi';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { openNotificationWithIcon } from '@/models/global';
import { ServiceResponse } from '@/services/service';
import { localeKeys } from '@/locales/pl-PL';

export interface IconProps {
  arg: boolean;
}

const Icon: FC<IconProps> = ({ arg }) =>
  arg ? (
    <CheckCircleTwoTone twoToneColor="#52C41A" />
  ) : (
    <CloseCircleTwoTone twoToneColor="#EB2F96" />
  );
function ChannelsListView() {
  const dispatch = useDispatch();
  const tableActionRef = useRef<ActionType>();

  function onEdit(id: number) {
    router.push(`/channels/edit/${id}`);
  }

  function onRemove(id: number) {
    dispatch({
      type: 'channels/remove',
      payload: {
        id,
        onResponse: (response: ServiceResponse<number>) => {
          if (response.status === 'failed') {
            openNotificationWithIcon(
              'error',
              formatMessage({ id: localeKeys.error }),
              formatMessage({ id: localeKeys.channels.list.failedRemove }),
            );
          }
          tableActionRef.current.reload();
        },
      },
    });
  }

  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<Channel>> {
    const response = await ChannelsService.fetchPage(props);
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

  const columns: ProColumns<Channel>[] = [
    {
      title: formatMessage({ id: localeKeys.channels.fields.name }),
      dataIndex: ['name', 'id'],
      render: (_, record: Channel) => <Link to={`/channels/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: localeKeys.channels.fields.email }),
      dataIndex: 'email',
      render: (email: boolean) => <Icon arg={email} />,
    },
    {
      title: formatMessage({ id: localeKeys.channels.fields.epuap }),
      dataIndex: 'epuap',
      render: (epuap: boolean) => <Icon arg={epuap} />,
    },
    {
      title: formatMessage({ id: localeKeys.channels.fields.city }),
      dataIndex: 'city',
      render: (city: boolean) => <Icon arg={city} />,
    },
    {
      title: formatMessage({ id: localeKeys.channels.fields.street }),
      dataIndex: 'street',
      render: (street: boolean) => <Icon arg={street} />,
    },
    {
      title: formatMessage({ id: localeKeys.channels.fields.houseNo }),
      dataIndex: 'houseNo',
      render: (houseNo: boolean) => <Icon arg={houseNo} />,
    },
    {
      title: formatMessage({ id: localeKeys.channels.fields.flatNo }),
      dataIndex: 'flatNo',
      render: (flatNo: boolean) => <Icon arg={flatNo} />,
    },
    {
      title: formatMessage({ id: localeKeys.channels.fields.postalCode }),
      dataIndex: 'postalCode',
      render: (postalCode: boolean) => <Icon arg={postalCode} />,
    },
    {
      title: formatMessage({ id: localeKeys.channels.fields.voivodeship }),
      dataIndex: 'voivodeship',
      render: (voivodeship: boolean) => <Icon arg={voivodeship} />,
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
      type="channels"
      columns={columns}
      fetchData={fetchPage}
      pageHeader={localeKeys.channels.list.pageHeaderContent}
      tableHeader={localeKeys.channels.list.table.header}
      actionRef={tableActionRef}
    />
  );
}

export default ChannelsListView;
