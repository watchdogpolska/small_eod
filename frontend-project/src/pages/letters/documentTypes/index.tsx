import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { connect } from 'dva';

import { DocumentType } from '@/services/documentTypes';
import Table from '@/components/Table';
import { PaginationParams, PaginationResponse } from '@/services/common';

const TableList: FC<{ dispatch: Function }> = ({ dispatch }) => {
  const fetchData = (parameter: PaginationParams): Promise<PaginationResponse<DocumentType>> => {
    return dispatch({ type: 'documentTypes/fetchPage', payload: parameter });
  };
  const columns: ProColumns<DocumentType>[] = [
    {
      title: formatMessage({ id: 'documentTypes-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
  ];

  return <Table type="documentTypes" columns={columns} fetchData={fetchData} />;
};

export default connect()(TableList);
