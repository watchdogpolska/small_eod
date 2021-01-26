import React, { FC, useEffect } from 'react';
import { Spin } from 'antd';
import { connect } from 'umi';

import { DocumentType } from '@/services/definitions';

export interface DocumentTypeNameProps {
  id: number;
  documentTypes: DocumentType[];
  dispatch: Function;
}

const DocumentTypeName: FC<DocumentTypeNameProps> = ({ id, documentTypes, dispatch }) => {
  useEffect(() => {
    dispatch({ type: 'documentTypes/fetchOne', payload: id });
  }, []);
  const oneDocumentType = documentTypes.find(value => value.id === id);
  if (!oneDocumentType) return <Spin />;
  return <>{oneDocumentType.name}</>;
};
export default connect(({ documentTypes }: DocumentTypeNameProps) => ({ documentTypes }))(
  DocumentTypeName,
);
