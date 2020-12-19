import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Tag } from '@/services/definitions';
import { TagsService } from '@/services/tags';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { useDispatch } from 'dva';
import { Link } from 'umi';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { openNotificationWithIcon } from '@/models/global';
import { ServiceResponse } from '@/services/service';
import { localeKeys } from '@/locales/pl-PL';

function TagsListView() {
  const dispatch = useDispatch();
  const tableActionRef = useRef<ActionType>();

  function onEdit(id: number) {
    router.push(`/tags/edit/${id}`);
  }

  function onRemove(id: number) {
    dispatch({
      type: 'tags/remove',
      payload: {
        id,
        onResponse: (response: ServiceResponse<number>) => {
          if (response.status === 'failed') {
            openNotificationWithIcon(
              'error',
              formatMessage({ id: localeKeys.error }),
              `${formatMessage({ id: localeKeys.tags.list.failedRemove })} ${id}`,
            );
          }
          tableActionRef.current.reload();
        },
      },
    });
  }

  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<Tag>> {
    const response = await TagsService.fetchPage(props);
    if (response.status === 'failed') {
      openNotificationWithIcon('error', formatMessage({ id: localeKeys.error }));
      return { data: [], total: 0 };
    }
    return response.data;
  }

  const columns: ProColumns<Tag>[] = [
    {
      title: formatMessage({ id: localeKeys.tags.fields.name }),
      dataIndex: ['name', 'id'],
      render: (_, record: Tag) => <Link to={`/tags/edit/${record.id}`}>{record.name}</Link>,
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
      type="cases"
      columns={columns}
      fetchData={fetchPage}
      pageHeader={localeKeys.tags.list.pageHeaderContent}
      tableHeader={localeKeys.tags.list.table.header}
      actionRef={tableActionRef}
    />
  );
}

export default TagsListView;
