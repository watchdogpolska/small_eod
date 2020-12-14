import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tag, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Case } from '@/services/definitions';
import { CasesService } from '@/services/cases';
import Table from '@/components/Table';
import InstitutionName from '@/components/Table/InstitutionName';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { useDispatch } from 'dva';
import { Link } from 'umi';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { openNotificationWithIcon } from '@/models/global';
import { ServiceResponse } from '@/services/service';
import { localeKeys } from '@/locales/pl-PL';

function CasesListView() {
  const dispatch = useDispatch();
  const tableActionRef = useRef<ActionType>();

  function onEdit(id: number) {
    router.push(`/cases/edit/${id}`);
  }

  function onRemove(id: number) {
    dispatch({
      type: 'cases/remove',
      payload: {
        id,
        onResponse: (response: ServiceResponse<number>) => {
          if (response.status === 'failed') {
            openNotificationWithIcon(
              'error',
              formatMessage({ id: localeKeys.error }),
              `${formatMessage({ id: localeKeys.cases.list.failedRemove })} ${id}`,
            );
          }
          tableActionRef.current.reload();
        },
      },
    });
  }

  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<Case>> {
    const response = await CasesService.fetchPage(props);
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

  const columns: ProColumns<Case>[] = [
    {
      title: formatMessage({ id: localeKeys.cases.fields.name }),
      dataIndex: ['name', 'id'],
      render: (_, record: Case) => <Link to={`/cases/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: localeKeys.cases.fields.auditedInstitutions }),
      dataIndex: 'auditedInstitutions',
      render: (auditedInstitutions: number[]) => (
        <>
          {auditedInstitutions.map(auditedInstitution => (
            <InstitutionName id={auditedInstitution} key={auditedInstitution} />
          ))}
        </>
      ),
    },
    {
      title: formatMessage({ id: localeKeys.cases.fields.comment }),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({ id: localeKeys.cases.fields.createdOn }),
      dataIndex: 'createdOn',
      render: createdOn => createdOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: localeKeys.cases.fields.modifiedOn }),
      dataIndex: 'modifiedOn',
      render: modifiedOn => modifiedOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: localeKeys.cases.fields.tags }),
      dataIndex: 'tags',
      render: (tags: number[]) => (
        <>
          {tags.map(tag => (
            <Tag color="blue" key={tag}>
              {tag}
            </Tag>
          ))}
        </>
      ),
    },
    {
      title: formatMessage({ id: localeKeys.cases.fields.letterCount }),
      dataIndex: 'letterCount',
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
      pageHeader={localeKeys.cases.list.pageHeaderContent}
      tableHeader={localeKeys.cases.list.table.header}
      actionRef={tableActionRef}
    />
  );
}

export default CasesListView;
