import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { Event, Case } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { EventsService } from '@/services/events';
import { FetchLink } from '@/components/FetchLink';
import { AutocompleteService } from '@/services/autocomplete';
import { openRemoveConfirmationModal } from '@/utils/utils';

export default function EventsListView(props: { case?: Case['id']; inline?: boolean }) {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.events;

  function onEdit(event: Event) {
    router.push(`/events/edit/${event.id}`);
  }

  function onRemove(event: Event) {
    openRemoveConfirmationModal(event.name, () =>
      EventsService.remove(event.id)
        .then(() => tableActionRef.current?.reload())
        .catch(() => tableActionRef.current?.reload()),
    );
  }

  const columns: ProColumns<Event>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'id',
      render: (_, record: Event) => <Link to={`/events/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: fields.case }),
      dataIndex: 'case',
      render: (_, record: Event) => (
        <FetchLink
          route="cases"
          id={record.case}
          autocompleteFunction={AutocompleteService.cases}
        />
      ),
    },
    {
      title: formatMessage({ id: fields.date }),
      dataIndex: 'date',
      render: (date: Date) => date.toLocaleString(),
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, record: Event) => (
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
      type="events"
      columns={columns}
      service={EventsService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
      filters={{ case: props.case }}
      inline={props.inline}
    />
  );
}
