import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { DocumentType } from '@/services/definitions';
import { DocumentTypesService } from '@/services/documentTypes';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { useDispatch } from 'dva';
import { Link } from 'umi';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { openNotificationWithIcon } from '@/models/global';
import { ServiceResponse } from '@/services/service';
import { localeKeys } from '@/locales/pl-PL';

function DocumentTypesListView() {
  const dispatch = useDispatch();
  const tableActionRef = useRef<ActionType>();

  function onEdit(id: number) {
    router.push(`/documentTypes/edit/${id}`);
  }

  function onRemove(id: number) {
    dispatch({
      type: 'documentTypes/remove',
      payload: {
        id,
        onResponse: (response: ServiceResponse<number>) => {
          if (response.status === 'failed') {
            openNotificationWithIcon(
              'error',
              formatMessage({ id: localeKeys.error }),
              `${formatMessage({ id: localeKeys.documentTypes.list.failedRemove })} ${id}`,
            );
          }
          tableActionRef.current.reload();
        },
      },
    });
  }

  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<DocumentType>> {
    const response = await DocumentTypesService.fetchPage(props);
    console.log(response);
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

  const columns: ProColumns<DocumentType>[] = [
    {
      title: formatMessage({ id: localeKeys.documentTypes.fields.name }),
      dataIndex: ['name', 'id'],
      render: (_, record: DocumentType) => (
        <Link to={`/documentTypes/edit/${record.id}`}>{record.name}</Link>
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
      type="cases"
      columns={columns}
      fetchData={fetchPage}
      pageHeader={localeKeys.documentTypes.list.pageHeaderContent}
      tableHeader={localeKeys.documentTypes.list.table.header}
      actionRef={tableActionRef}
    />
  );
}

export default DocumentTypesListView;
