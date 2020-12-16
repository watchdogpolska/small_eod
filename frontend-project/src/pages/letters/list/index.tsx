import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { fetchLettersPage } from '@/services/letters';
import { Letter } from '@/services/definitions';
import Table from '@/components/Table';
import ChannelName from '@/components/Table/ChannelName';
import InstitutionName from '@/components/Table/InstitutionName';
import CaseName from '@/components/Table/CaseName';
import DocumentTypeName from '@/components/Table/DocumentTypeName';

const TableList: FC<{}> = () => {
  const columns: ProColumns<Letter>[] = [
    {
      title: formatMessage({ id: 'letters-list.table.columns.documentType.title' }),
      dataIndex: 'documentType',
      render: (documentType: number | string) =>
        typeof documentType === 'number' ? <DocumentTypeName id={documentType} /> : documentType,
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.referenceNumber.title' }),
      dataIndex: 'referenceNumber',
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.comment.title' }),
      dataIndex: 'comment',
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.direction.title' }),
      dataIndex: 'direction',
      render: (direction: string) =>
        formatMessage({ id: `letters-list.table.direction.${direction.toLowerCase()}` }),
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.channel.title' }),
      dataIndex: 'channel',
      render: (channel: number | string) =>
        typeof channel === 'number' ? <ChannelName id={channel} /> : channel,
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.date.title' }),
      dataIndex: 'date',
      render: (date: string) => date.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.case.title' }),
      dataIndex: 'case',
      render: (_case: number | string) =>
        typeof _case === 'number' ? <CaseName id={_case} /> : _case,
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.audited_institution.title' }),
      dataIndex: 'institution',
      render: (institution: number | string) =>
        typeof institution === 'number' ? <InstitutionName id={institution} /> : institution,
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.createdOn.title' }),
      dataIndex: 'createdOn',
      render: createdOn => createdOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.modifiedOn.title' }),
      dataIndex: 'modifiedOn',
      render: modifiedOn => modifiedOn.toLocaleString(),
    },
    {
      title: formatMessage({ id: 'letters-list.table.columns.attachments.title' }),
      dataIndex: 'attachments',
      render: (attachments: []) => attachments.length,
    },
  ];

  return <Table type="letters" columns={columns} fetchData={fetchLettersPage} />;
};

export default TableList;
