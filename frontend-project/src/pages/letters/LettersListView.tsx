import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef, useState } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { Case, Letter, File } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { LettersService } from '@/services/letters';
import { FetchLink } from '@/components/FetchLink';
import { AutocompleteService } from '@/services/autocomplete';
import { FileCard } from '@/components/FileCard/FileCard';
import { FileService } from '@/services/files';

const MemoLetterExpandedRow = React.memo(LetterExpandedRow);
function LetterExpandedRow(props: { letter: Letter }) {
  const [attachments, setAttachments] = useState(props.letter.attachments);
  function onAttachmentRemove(fileId: File['id']) {
    return FileService(props.letter)
      .remove(fileId)
      .then(() => setAttachments(files => files.filter(file => file.id !== fileId)));
  }
  return (
    <div style={{ display: 'flex' }}>
      {attachments.map(attachment => (
        <FileCard
          key={attachment.id}
          file={attachment}
          onRemove={() => onAttachmentRemove(attachment.id)}
        />
      ))}
    </div>
  );
}

export default function LettersListView(props: { case?: Case['id']; inline?: boolean }) {
  const tableActionRef = useRef<ActionType>();
  const { fields, list, directions } = localeKeys.letters;

  function onEdit(id: number) {
    router.push(`/letters/edit/${id}`);
  }

  function onRemove(id: number) {
    LettersService.remove(id)
      .then(() => tableActionRef.current?.reload())
      .catch(() => tableActionRef.current?.reload());
  }

  const columns: ProColumns<Letter>[] = [
    {
      title: formatMessage({ id: fields.referenceNumber }),
      dataIndex: 'id',
      render: (_, record: Letter) => (
        <Link to={`/letters/edit/${record.id}`}>{record.referenceNumber}</Link>
      ),
    },
    {
      title: formatMessage({ id: fields.documentType }),
      dataIndex: 'documentType',
      render: (_, record: Letter) => (
        <FetchLink
          route="documentTypes"
          id={record.documentType}
          autocompleteFunction={AutocompleteService.documentTypes}
        />
      ),
    },
    {
      title: formatMessage({ id: fields.comment }),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({ id: fields.direction }),
      dataIndex: 'direction',
      render: (direction: string) =>
        formatMessage({ id: direction === 'IN' ? directions.in : directions.out }),
    },
    {
      title: formatMessage({ id: fields.channel }),
      dataIndex: 'channel',
      render: (_, record: Letter) => (
        <FetchLink
          route="channels"
          id={record.channel}
          autocompleteFunction={AutocompleteService.channels}
        />
      ),
    },
    {
      title: formatMessage({ id: fields.date }),
      dataIndex: 'date',
      render: (date: string) => date.toLocaleString(),
    },
    {
      title: formatMessage({ id: fields.case }),
      dataIndex: 'case',
      render: (_, record: Letter) => (
        <FetchLink
          route="cases"
          id={record.case}
          autocompleteFunction={AutocompleteService.cases}
        />
      ),
    },
    {
      title: formatMessage({ id: fields.institution }),
      dataIndex: 'institution',
      render: (_, record: Letter) => (
        <FetchLink
          route="institutions"
          id={record.institution}
          autocompleteFunction={AutocompleteService.institutions}
        />
      ),
    },
    {
      title: formatMessage({ id: fields.createdOn }),
      dataIndex: 'createdOn',
      render: createdOn => createdOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: fields.modifiedOn }),
      dataIndex: 'modifiedOn',
      render: modifiedOn => modifiedOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: fields.numberAttachments }),
      dataIndex: 'attachments',
      render: (attachments: []) => attachments.length,
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
      type="letters"
      columns={columns}
      service={LettersService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
      expandable={{
        expandedRowRender: record => <MemoLetterExpandedRow letter={record} />,
      }}
      filters={{ case: props.case }}
      inline={props.inline}
    />
  );
}
