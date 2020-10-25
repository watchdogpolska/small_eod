import { notification } from 'antd';
import { ReactNode } from 'react';
import { IconType } from 'antd/lib/notification';

export const openNotificationWithIcon = (message: IconType, description: ReactNode) => {
  notification[message]({ message, description });
};
