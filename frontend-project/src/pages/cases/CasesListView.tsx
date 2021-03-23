import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tag, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { CaseList } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { CasesService } from '@/services/cases';

export default function CaseListsListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.cases;

  function onEdit(id: number) {
    router.push(`/cases/edit/${id}`);
  }

  function onRemove(id: number) {
    CasesService.remove(id)
      .then(() => tableActionRef.current?.reload())
      .catch(() => tableActionRef.current?.reload());
  }

  const columns: ProColumns<CaseList>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'id',
      render: (_, record: CaseList) => <Link to={`/cases/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: fields.auditedInstitutions }),
      dataIndex: 'auditedInstitutions',
      render: (_, record) => (
        <>
          {record.auditedInstitutions.map(auditedInstitution => (
            <Tag key={auditedInstitution}>{auditedInstitution}</Tag>
          ))}
        </>
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
      render: modifiedOn => modifiedOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: fields.tags }),
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
      title: formatMessage({ id: fields.letterCount }),
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
      service={CasesService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
