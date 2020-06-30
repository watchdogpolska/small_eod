import React, { FC, useEffect, useState } from 'react';
import { Spin } from 'antd';
import { Channel } from '@/models/channels';

export const ChannelName: FC<{ id: number }> = props => {
  const [name, setName] = useState('');
  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchChannel(props.id);
      setName(result.name);
    };
    fetchData();
  }, []);

  return name ? <div>{name}</div> : <Spin />;
};
