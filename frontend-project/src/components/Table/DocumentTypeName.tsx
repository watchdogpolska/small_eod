import React, { FC, useEffect } from 'react';
import { Spin } from 'antd';
import { connect } from 'dva';

import { DocumentType } from '@/models/documentTypes';

export interface DocumentTypeNameProps {
  id: number;
  documentTypes: DocumentType[];
  dispatch: Function;
}

const DocumentTypeName: FC<DocumentTypeNameProps> = ({ id, documentTypes, dispatch }) => {
  useEffect(() => {
    dispatch({ type: 'documentTypes/fetchOne', payload: id });
  }, []);
  const documentType = documentTypes.find(value => value.id === id);

  return <div>{documentType ? documentType.name : <Spin />}</div>;
};
export default connect(({ documentTypes }: DocumentTypeNameProps) => ({ documentTypes }))(
  DocumentTypeName,
);
