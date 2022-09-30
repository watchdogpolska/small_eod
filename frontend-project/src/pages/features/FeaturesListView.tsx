import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { Feature } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { FeaturesService } from '@/services/features';
import { openRemoveConfirmationModal } from '@/utils/utils';

export default function FeaturesListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.features;

  function onEdit(feature: Feature) {
    router.push(`/features/edit/${feature.id}`);
  }

  function onRemove(feature: Feature) {
    openRemoveConfirmationModal(feature.name, () =>
      FeaturesService.remove(feature.id).then(
        () => tableActionRef.current?.reload(),
        () => tableActionRef.current?.reload(),
      ),
    );
  }

  const columns: ProColumns<Feature>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'name',
      render: (_, record: Feature) => <Link to={`/features/edit/${record.id}`}>{record.name}</Link>,
    },
    {
      title: formatMessage({ id: fields.minOptions }),
      dataIndex: 'minOptions',
    },
    {
      title: formatMessage({ id: fields.maxOptions }),
      dataIndex: 'maxOptions',
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, record: Feature) => (
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
      type="features"
      columns={columns}
      service={FeaturesService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
