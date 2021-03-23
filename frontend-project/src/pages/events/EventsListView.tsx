import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { EventList } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { EventsService } from '@/services/events';

export default function EventsListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.events;

  function onEdit(id: number) {
    router.push(`/events/edit/${id}`);
  }

  function onRemove(id: number) {
    EventsService.remove(id)
      .then(() => tableActionRef.current?.reload())
      .catch(() => tableActionRef.current?.reload());
  }

  const columns: ProColumns<EventList>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'id',
      render: (_, record: EventList) => <Link to={`/events/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: fields.case }),
      dataIndex: 'case',
      render: (_, record: EventList) => record.case,
    },
    {
      title: formatMessage({ id: fields.date }),
      dataIndex: 'date',
      render: (date: Date) => date.toLocaleString(),
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
      type="events"
      columns={columns}
      service={EventsService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
