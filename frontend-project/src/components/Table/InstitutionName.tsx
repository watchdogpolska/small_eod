import React, { FC, useEffect } from 'react';
import { Spin } from 'antd';
import { connect } from 'dva';

import { Institution } from '@/models/institutions';

export interface InstitutionNameProps {
  id: number;
  institutions: Institution[];
  dispatch: Function;
}

const InstitutionName: FC<InstitutionNameProps> = ({ id, institutions, dispatch }) => {
  useEffect(() => {
    // dispatch({ type: 'institutions/fetchOne', payload: id });
  }, []);
  console.log('ok');

  return <div>ok</div>;
};

export default connect(({ institutions }: any) => ({ institutions }))(InstitutionName);
