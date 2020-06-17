import React, { FC, useEffect, useState } from 'react';
import { Spin } from 'antd';

import { fetchInstitution } from '@/services/institutions';

export const InstitutionName: FC<{ id: number }> = props => {
  const [name, setName] = useState('');
  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchInstitution(props.id);
      setName(result.name);
    };
    fetchData();
  }, []);

  return name ? <div>{name}</div> : <Spin />;
};
