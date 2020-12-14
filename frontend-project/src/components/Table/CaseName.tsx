import React, { FC, useEffect } from 'react';
import { Spin } from 'antd';
import { connect, useDispatch } from 'dva';

import { Case } from '@/services/definitions';
import { ReduxResourceState } from '@/utils/reduxModel';

export interface CaseNameProps {
  id: number;
  cases: ReduxResourceState<Case>;
}

const CaseName: FC<CaseNameProps> = ({ id, cases }) => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch({ type: 'cases/fetchOne', payload: { id } });
  }, []);
  const oneCase = cases.data.find(value => value.id === id);
  if (!oneCase) return <Spin />;

  return <>{oneCase.name}</>;
};

export default connect(({ cases }: CaseNameProps) => ({ cases }))(CaseName);
