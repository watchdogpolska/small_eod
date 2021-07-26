import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { Tag } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { TagsService } from '@/services/tags';
import { openRemoveConfirmationModal } from '@/utils/utils';

export default function TagsListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.tags;

  function onEdit(tag: Tag) {
    router.push(`/tags/edit/${tag.id}`);
  }

  function onRemove(tag: Tag) {
    openRemoveConfirmationModal(tag.name, () =>
      TagsService.remove(tag.id)
        .then(() => tableActionRef.current?.reload())
        .catch(() => tableActionRef.current?.reload()),
    );
  }

  const columns: ProColumns<Tag>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'id',
      render: (_, record: Tag) => <Link to={`/tags/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, record: Tag) => (
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
      type="tags"
      columns={columns}
      service={TagsService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
