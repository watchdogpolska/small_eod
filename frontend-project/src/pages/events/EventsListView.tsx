import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Event } from '@/services/definitions';
import { EventsService } from '@/services/events';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { useDispatch } from 'dva';
import { Link } from 'umi';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { openNotificationWithIcon } from '@/models/global';
import { ServiceResponse } from '@/services/service';
import { localeKeys } from '@/locales/pl-PL';
import CaseName from '@/components/Table/CaseName';

function EventsListView() {
  const dispatch = useDispatch();
  const tableActionRef = useRef<ActionType>();

  function onEdit(id: number) {
    router.push(`/events/edit/${id}`);
  }

  function onRemove(id: number) {
    dispatch({
      type: 'events/remove',
      payload: {
        id,
        onResponse: (response: ServiceResponse<number>) => {
          if (response.status === 'failed') {
            openNotificationWithIcon(
              'error',
              formatMessage({ id: localeKeys.error }),
              `${formatMessage({ id: localeKeys.events.list.failedRemove })} ${id}`,
            );
          }
          tableActionRef.current.reload();
        },
      },
    });
  }

  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<Event>> {
    const response = await EventsService.fetchPage(props);
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

  const columns: ProColumns<Event>[] = [
    {
      title: formatMessage({ id: localeKeys.events.fields.name }),
      dataIndex: ['name', 'id'],
      render: (_, record: Event) => <Link to={`/events/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: localeKeys.events.fields.case }),
      dataIndex: 'case',
      render: (_, record: Event) => <CaseName id={record.case} />,
    },
    {
      title: formatMessage({ id: localeKeys.events.fields.date }),
      dataIndex: 'date',
      render: (_, record: Event) => record.date.toLocaleString(),
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
      fetchData={fetchPage}
      pageHeader={localeKeys.events.list.pageHeaderContent}
      tableHeader={localeKeys.events.list.table.header}
      actionRef={tableActionRef}
    />
  );
}

export default EventsListView;
