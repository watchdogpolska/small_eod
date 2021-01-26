import React, { FC, useEffect } from 'react';
import { connect } from 'umi';

import { Spin } from 'antd';
import { Channel } from '@/services/definitions';

export interface ChannelNameProps {
  id: number;
  channels: Channel[];
  dispatch: Function;
}

const ChannelName: FC<ChannelNameProps> = ({ id, channels, dispatch }) => {
  useEffect(() => {
    dispatch({ type: 'channels/fetchOne', payload: id });
  }, []);
  const oneChannel = channels.find(value => value.id === id);
  if (!oneChannel) return <Spin />;
  return <>{oneChannel.name}</>;
};
export default connect(({ channels }: ChannelNameProps) => ({ channels }))(ChannelName);
