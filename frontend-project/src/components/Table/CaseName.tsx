import React, { FC, useEffect, useState } from 'react';
import { Spin } from 'antd';

import { fetchCase } from '@/services/cases';

export const CaseName: FC<{ id: number }> = props => {
  const [name, setName] = useState('');
  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchCase(props.id);
      setName(result.name);
    };
    fetchData();
  }, []);

  return name ? <div>{name}</div> : <Spin />;
};
