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
import Table from '@/components/Table';
import router from 'umi/router';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { ChannelsService } from '@/services/channels';
import { openRemoveConfirmationModal } from '@/utils/utils';

export interface IconProps {
  arg: boolean;
}

const Icon: FC<IconProps> = ({ arg }) =>
  arg ? (
    <CheckCircleTwoTone twoToneColor="#52C41A" />
  ) : (
    <CloseCircleTwoTone twoToneColor="#EB2F96" />
  );
export default function ChannelsListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.channels;

  function onEdit(channel: Channel) {
    router.push(`/channels/edit/${channel.id}`);
  }

  function onRemove(channel: Channel) {
    openRemoveConfirmationModal(channel.name, () =>
      ChannelsService.remove(channel.id)
        .then(() => tableActionRef.current?.reload())
        .catch(() => tableActionRef.current?.reload()),
    );
  }

  const columns: ProColumns<Channel>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'id',
      render: (_, record: Channel) => <Link to={`/channels/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: fields.email }),
      dataIndex: 'email',
      render: (email: boolean) => <Icon arg={email} />,
    },
    {
      title: formatMessage({ id: fields.epuap }),
      dataIndex: 'epuap',
      render: (epuap: boolean) => <Icon arg={epuap} />,
    },
    {
      title: formatMessage({ id: fields.city }),
      dataIndex: 'city',
      render: (city: boolean) => <Icon arg={city} />,
    },
    {
      title: formatMessage({ id: fields.street }),
      dataIndex: 'street',
      render: (street: boolean) => <Icon arg={street} />,
    },
    {
      title: formatMessage({ id: fields.houseNo }),
      dataIndex: 'houseNo',
      render: (houseNo: boolean) => <Icon arg={houseNo} />,
    },
    {
      title: formatMessage({ id: fields.flatNo }),
      dataIndex: 'flatNo',
      render: (flatNo: boolean) => <Icon arg={flatNo} />,
    },
    {
      title: formatMessage({ id: fields.postalCode }),
      dataIndex: 'postalCode',
      render: (postalCode: boolean) => <Icon arg={postalCode} />,
    },
    {
      title: formatMessage({ id: fields.voivodeship }),
      dataIndex: 'voivodeship',
      render: (voivodeship: boolean) => <Icon arg={voivodeship} />,
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, record: Channel) => (
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
      type="channels"
      columns={columns}
      service={ChannelsService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
