import React, { FC, useEffect } from 'react';
import { connect } from 'dva';

import { Spin } from 'antd';
import { Channel } from '@/services/channels';

export interface ChannelNameProps {
  id: number;
  channels: Channel[];
  dispatch: Function;
}

const ChannelName: FC<ChannelNameProps> = ({ id, channels, dispatch }) => {
  useEffect(() => {
    dispatch({ type: 'channels/fetchOne', payload: id });
  }, []);
  const channel = channels.find(value => value.id === id);
  return <div>{channel ? channel.name : <Spin />}</div>;
};
export default connect(({ channels }: any) => ({ channels }))(ChannelName);
