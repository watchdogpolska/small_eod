import React, { FC, useEffect, useState } from 'react';

import { fetchInstitution } from '@/services/institutions';

export const Institution: FC<{ id: number }> = props => {
  const [name, setName] = useState('');
  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchInstitution(props.id);
      setName(result.name);
    };
    fetchData();
  }, []);

  return <div>{name}</div>;
};
