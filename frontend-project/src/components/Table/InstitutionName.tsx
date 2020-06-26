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
  const institution = institutions.find(value => value.id === id);
  useEffect(() => {
    if (!institution) {
      dispatch({ type: 'institutions/fetchOne', payload: id });
    }
  }, []);
  return <div>{institution ? institution.name : <Spin />}</div>;
};

export default connect(({ institutions }: any) => ({ institutions }))(InstitutionName);
