import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';

import { DocumentType, fetchDocumentTypesPage } from '@/services/documentTypes';
import Table from '@/components/Table';

const TableList: FC<{}> = () => {
  const columns: ProColumns<DocumentType>[] = [
    {
      title: formatMessage({ id: 'documentTypes-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
  ];

  return <Table type="documentTypes" columns={columns} fetchData={fetchDocumentTypesPage} />;
};

export default TableList;
