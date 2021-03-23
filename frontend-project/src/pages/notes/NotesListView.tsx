import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { NoteList } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { NotesService } from '@/services/notes';

export default function NotesListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.notes;

  function onEdit(id: number) {
    router.push(`/notes/edit/${id}`);
  }

  function onRemove(id: number) {
    NotesService.remove(id)
      .then(() => tableActionRef.current?.reload())
      .catch(() => tableActionRef.current?.reload());
  }

  const columns: ProColumns<NoteList>[] = [
    {
      title: formatMessage({ id: fields.id }),
      dataIndex: 'id',
      render: (_, record: NoteList) => <Link to={`/notes/edit/${record.id}`}>{record.id}</Link>,
    },
    {
      title: formatMessage({ id: fields.case }),
      dataIndex: 'case',
      render: (_, record: NoteList) => <>{record.case}</>,
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
      type="notes"
      columns={columns}
      service={NotesService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
