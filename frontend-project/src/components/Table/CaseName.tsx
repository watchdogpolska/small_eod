import React, { FC, useEffect } from 'react';
import { Spin } from 'antd';
import { connect } from 'dva';

import { Case } from '@/models/cases';

export interface CaseNameProps {
  id: number;
  cases: Case[];
  dispatch: Function;
}

const CaseName: FC<CaseNameProps> = ({ id, cases, dispatch }) => {
  const oneCase = cases.find(value => value.id === id);
  useEffect(() => {
    if (!oneCase) {
      dispatch({ type: 'cases/fetchOne', payload: id });
    }
  }, []);
  console.log(oneCase);
  return <div>{oneCase ? oneCase.name : <Spin />}</div>;
};

export default connect(({ cases }: any) => ({ cases }))(CaseName);
