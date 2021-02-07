import React, { FC, useEffect } from 'react';
import { Spin } from 'antd';
import { connect, useDispatch } from 'dva';
import { ReduxResourceState } from '@/utils/reduxModel';
import { DocumentType } from '@/services/definitions';

export interface DocumentTypeNameProps {
  id: number;
  documentTypes: ReduxResourceState<DocumentType>;
}

const DocumentTypeName: FC<DocumentTypeNameProps> = ({ id, documentTypes }) => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch({ type: 'documentTypes/fetchOne', payload: { id } });
  }, []);
  const oneCase = documentTypes.data.find(value => value.id === id);
  if (!oneCase) return <Spin />;

  return <>{oneCase.name}</>;
};
export default connect(({ documentTypes }: DocumentTypeNameProps) => ({ documentTypes }))(
  DocumentTypeName,
);
