import { ActionType, ProColumns } from '@ant-design/pro-table';
import { Button, Space, Tooltip } from 'antd';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { FeatureOption } from '@/services/definitions';
import Table from '@/components/Table';
import router from 'umi/router';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { FeatureOptionsService } from '@/services/featureOptions';
import { FetchLink } from '@/components/FetchLink';
import { AutocompleteService } from '@/services/autocomplete';
import { openRemoveConfirmationModal } from '@/utils/utils';

export default function FeatureOptionsListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.featureOptions;

  function onEdit(featureOption: FeatureOption) {
    router.push(`/featureOptions/edit/${featureOption.id}`);
  }

  function onRemove(featureOption: FeatureOption) {
    openRemoveConfirmationModal(featureOption.name, () =>
      FeatureOptionsService.remove(featureOption.id)
        .then(() => tableActionRef.current?.reload())
        .catch(() => tableActionRef.current?.reload()),
    );
  }

  const columns: ProColumns<FeatureOption>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'name',
      render: (_, record: FeatureOption) => (
        <Link to={`/featureOptions/edit/${record.id}`}>{record.name}</Link>
      ),
    },
    {
      title: formatMessage({ id: fields.feature }),
      dataIndex: 'feature',
      render: (_, record: FeatureOption) => (
        <FetchLink
          route="features"
          id={record.feature}
          autocompleteFunction={AutocompleteService.features}
        />
      ),
    },
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, record: FeatureOption) => (
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
      type="featureOptions"
      columns={columns}
      service={FeatureOptionsService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
