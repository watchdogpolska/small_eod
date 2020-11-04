import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import Table from '@/components/Table';
import { fetchAdministrativeUnitsPage } from '@/services/administrativeUnits';
import { AdministrativeUnit } from '@/services/definitions';
import CheckIcon from '@/components/Icons/checkIcon';
import AdministrativeUnitParent from './parent';

const TableList: FC<{}> = () => {
  const columns: ProColumns<AdministrativeUnit>[] = [
    {
      title: formatMessage({ id: 'administrative-units-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
    {
      title: formatMessage({ id: 'administrative-units-list.table.columns.category.title' }),
      dataIndex: 'category',
    },
    {
      title: formatMessage({ id: 'administrative-units-list.table.columns.slug.title' }),
      dataIndex: 'slug',
    },
    {
      title: formatMessage({ id: 'administrative-units-list.table.columns.updatedOn.title' }),
      dataIndex: 'updatedOn',
      render: updatedOn => updatedOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'administrative-units-list.table.columns.active.title' }),
      dataIndex: 'active',
      render: (active: boolean) => <CheckIcon arg={active} />,
    },
    {
      title: formatMessage({ id: 'administrative-units-list.table.columns.active.parent' }),
      dataIndex: 'parent',
      render: (parent: string | null) => <AdministrativeUnitParent id={parent} />,
    },
  ];

  return (
    <Table type="administrative-units" columns={columns} fetchData={fetchAdministrativeUnitsPage} />
  );
};

export default TableList;
