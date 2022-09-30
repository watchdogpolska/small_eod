import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { DocumentType } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { DocumentTypesService } from '@/services/documentTypes';
import { openRemoveConfirmationModal } from '@/utils/utils';

export default function DocumentTypesListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.documentTypes;

  function onEdit(documentType: DocumentType) {
    router.push(`/documentTypes/edit/${documentType.id}`);
  }

  function onRemove(documentType: DocumentType) {
    openRemoveConfirmationModal(documentType.name, () =>
      DocumentTypesService.remove(documentType.id)
        .then(() => tableActionRef.current?.reload())
        .catch(() => tableActionRef.current?.reload()),
    );
  }

  const columns: ProColumns<DocumentType>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'id',
      render: (_, record: DocumentType) => (
        <Link to={`/documentTypes/edit/${record.id}`}>{record.name}</Link>
      ),
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, record: DocumentType) => (
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
      type="cases"
      columns={columns}
      service={DocumentTypesService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
