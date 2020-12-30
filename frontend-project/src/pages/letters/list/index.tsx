import { ActionType, ProColumns } from '@ant-design/pro-table';
import React, { FC, useRef } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { Letter } from '@/services/definitions';
import Table from '@/components/Table';
import ChannelName from '@/components/Table/ChannelName';
import InstitutionName from '@/components/Table/InstitutionName';
import CaseName from '@/components/Table/CaseName';
import DocumentTypeName from '@/components/Table/DocumentTypeName';
import { Button, Space, Tooltip } from 'antd';
import { DeleteOutlined } from '@ant-design/icons';
import { useDispatch } from 'dva';
import { openNotificationWithIcon } from '@/models/global';
import { ServiceResponse } from '@/services/service';
import { PaginationParams, PaginationResponse } from '@/services/common';
import { LettersService } from '@/services/letters';
import { localeKeys } from '@/locales/pl-PL';
import { useConfirmationModal } from '@/components/Modals/Confirmation';

const TableList: FC<{}> = () => {
  const dispatch = useDispatch();
  const tableActionRef = useRef<ActionType>();

  function onRemove(id: number): Promise<void> {
    return new Promise((resolve, reject) => {
      dispatch({
        type: 'letters/remove',
        payload: {
          id,
          onResponse: (response: ServiceResponse<number>) =>
            response.status === 'failed' ? reject() : resolve(),
        },
      });
    });
  }

  const [modal, showModal] = useConfirmationModal(
    {
      onSuccess: () => tableActionRef.current.reload(),
      onFailure: id =>
        openNotificationWithIcon(
          'error',
          formatMessage({ id: localeKeys.error }),
          `${formatMessage({ id: 'letters-list.table.notification.remove' })} ${id}`,
        ),
    },
    onRemove,
  );

  async function fetchPage(props: PaginationParams): Promise<PaginationResponse<Letter>> {
    const response = await LettersService.fetchPage(props);
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
    {
      title: formatMessage({ id: localeKeys.lists.actions }),
      dataIndex: 'id',
      render: (_, { id, referenceNumber }: Letter) => (
        <Space>
          <Tooltip title={formatMessage({ id: localeKeys.lists.delete })}>
            <Button
              type="default"
              danger
              shape="circle"
              icon={<DeleteOutlined />}
              onClick={() =>
                showModal(
                  id,
                  formatMessage(
                    {
                      id: 'letters-list.table.modal.remove.title',
                    },
                    {
                      referenceNumber: referenceNumber || '',
                    },
                  ),
                )
              }
            />
          </Tooltip>
        </Space>
      ),
    },
  ];

  return (
    <>
      <Table type="letters" columns={columns} actionRef={tableActionRef} fetchData={fetchPage} />
      {modal}
    </>
  );
};

export default TableList;
