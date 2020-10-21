import React, { FC, useEffect } from 'react';
import { Spin } from 'antd';
import { connect } from 'dva';

import { Institution } from '@/services/definitions';

export interface InstitutionNameProps {
  id: number;
  institutions: Institution[];
  dispatch: Function;
}

const InstitutionName: FC<InstitutionNameProps> = ({ id, institutions, dispatch }) => {
  useEffect(() => {
    dispatch({ type: 'institutions/fetchOne', payload: id });
  }, []);
  const institution = institutions.find(value => value.id === id);
  return <div>{institution ? institution.name : <Spin />}</div>;
};

export default connect(({ institutions }: InstitutionNameProps) => ({ institutions }))(
  InstitutionName,
);
