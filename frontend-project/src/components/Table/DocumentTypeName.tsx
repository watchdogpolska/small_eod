import React, { FC, useEffect, useState } from 'react';
import { Spin } from 'antd';

import { fetchDocumentType } from '@/services/documentTypes';

export const DocumentTypeName: FC<{ id: number }> = props => {
  const [name, setName] = useState('');
  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchDocumentType(props.id);
      setName(result.name);
    };
    fetchData();
  }, []);
  return name ? <div>{name}</div> : <Spin />;
};
