import { notification } from 'antd';
import { IconType } from 'antd/lib/notification';

export interface GlobalModelState {
  collapsed: boolean;
}

export const openNotificationWithIcon = (message: IconType, title: string, description: string) => {
  notification[message]({ message: title, description });
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
