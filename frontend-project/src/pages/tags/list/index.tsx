import { ProColumns } from '@ant-design/pro-table';
import React, { FC } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { connect } from 'dva';

import { Tag } from '@/services/tags';
import Table from '@/components/Table';
import { PaginationParams, PaginationResponse } from '@/services/common.d';

const TableList: FC<{ dispatch: Function }> = ({ dispatch }) => {
  const fetchData = (parameter: PaginationParams): Promise<PaginationResponse<Tag>> => {
    return dispatch({ type: 'tags/fetchPage', payload: parameter });
  };

  const columns: ProColumns<Tag>[] = [
    {
      title: formatMessage({ id: 'tags-list.table.columns.name.title' }),
      dataIndex: 'name',
    },
  ];
  return <Table type="tags" columns={columns} fetchData={fetchData} />;
};

export default connect()(TableList);
