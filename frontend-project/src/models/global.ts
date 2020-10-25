import { notification } from 'antd';
import { ReactNode } from 'react';
import { IconType } from 'antd/lib/notification';

export interface GlobalModelState {
  collapsed: boolean;
}
export const openNotificationWithIcon = (message: IconType, description: ReactNode) => {
  notification[message]({ message, description });
};
const GlobalModel = {
  namespace: 'global',
  state: {
    collapsed: false,
  },

  reducers: {
    changeLayoutCollapsed(state = { notices: [], collapsed: true }, { payload }): GlobalModelState {
      return {
        ...state,
        collapsed: payload,
      };
    },
  },
};

export default GlobalModel;
