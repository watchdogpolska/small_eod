import { ActionType, ProColumns } from '@ant-design/pro-table';
import React, { useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { AdministrativeUnit } from '@/services/definitions';
import Table from '@/components/Table';
import { Link } from 'umi';
import { localeKeys } from '@/locales/pl-PL';
import { AdministrativeUnitsService } from '@/services/administrativeUnits';

export default function AdministrativeUnitsListView() {
  const tableActionRef = useRef<ActionType>();
  const { fields, list } = localeKeys.administrativeUnits;

  const columns: ProColumns<AdministrativeUnit>[] = [
    {
      title: formatMessage({ id: fields.name }),
      dataIndex: 'id',
      render: (_, record: AdministrativeUnit) => (
        <Link to={`/administrativeUnits/edit/${record.id}`}>{record.name}</Link>
      ),
    },
  ];
  return (
    <Table
      type="administrativeUnits"
      columns={columns}
      service={AdministrativeUnitsService}
      pageHeader={list.pageHeaderContent}
      tableHeader={list.table.header}
      actionRef={tableActionRef}
    />
  );
}
