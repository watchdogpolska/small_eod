import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tag, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { Institution } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { InstitutionsService } from '@/services/institutions';

export default function InstitutionsListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.institutions;

  function onEdit(id: number) {
    router.push(`/institutions/edit/${id}`);
  }

  function onRemove(id: number) {
    InstitutionsService.remove(id)
      .then(() => tableActionRef.current?.reload())
      .catch(() => tableActionRef.current?.reload());
  }

  const columns: ProColumns<Institution>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'name',
      render: (_, record: Institution) => (
        <Link to={`/institutions/edit/${record.id}`}>{record.name}</Link>
      ),
    },
    {
      title: formatMessage({ id: fields.comment }),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({ id: fields.createdOn }),
      dataIndex: 'createdOn',
      render: createdOn => createdOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: fields.modifiedOn }),
      dataIndex: 'modifiedOn',
      render: (modifiedOn: string) => modifiedOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: fields.tags }),
      dataIndex: 'tags',
      render: (tags: number[]) => (
        <>
          {tags.map(tag => (
            <Tag color="default" key={tag}>
              {tag}
            </Tag>
          ))}
        </>
      ),
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
      type="institutions"
      columns={columns}
      service={InstitutionsService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
