import React, { FC, useEffect } from 'react';
import { Spin } from 'antd';
import { connect } from 'umi';
import type { Dispatch } from 'umi';

import { Institution } from '@/services/definitions';

export interface InstitutionNameProps {
  id: number;
  institutions: Institution[];
  dispatch: Dispatch;
}

const InstitutionName: FC<InstitutionNameProps> = ({ id, institutions, dispatch }) => {
  useEffect(() => {
    dispatch({ type: 'institutions/fetchOne', payload: id });
  }, []);
  const oneInstitution = institutions.find(value => value.id === id);
  if (!oneInstitution) return <Spin />;
  return <>{oneInstitution.name}</>;
};

export default connect(({ institutions }: InstitutionNameProps) => ({ institutions }))(
  InstitutionName,
);
