import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { Note, Case } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { NotesService } from '@/services/notes';
import { FetchLink } from '@/components/FetchLink';
import { AutocompleteService } from '@/services/autocomplete';
import { openRemoveConfirmationModal } from '@/utils/utils';

export default function NotesListView(props: { case?: Case['id']; inline?: boolean }) {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.notes;

  function onEdit(note: Note) {
    router.push(`/notes/edit/${note.id}`);
  }

  function onRemove(note: Note) {
    openRemoveConfirmationModal(String(note.id), () =>
      NotesService.remove(note.id)
        .then(() => tableActionRef.current?.reload())
        .catch(() => tableActionRef.current?.reload()),
    );
  }

  const columns: ProColumns<Note>[] = [
    {
      title: formatMessage({ id: fields.id }),
      dataIndex: 'id',
      render: (_, record: Note) => <Link to={`/notes/edit/${record.id}`}>{record.id}</Link>,
    },
    {
      title: formatMessage({ id: fields.case }),
      dataIndex: 'case',
      render: (_, record: Note) => (
        <FetchLink
          route="cases"
          id={record.case}
          autocompleteFunction={AutocompleteService.cases}
        />
      ),
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, record: Note) => (
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
      type="notes"
      columns={columns}
      service={NotesService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
      expandable={{
        expandedRowRender: record => <>{record.comment}</>,
      }}
      filters={{ case: props.case }}
      inline={props.inline}
    />
  );
}
