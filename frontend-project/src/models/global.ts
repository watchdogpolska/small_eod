import { notification } from 'antd';

export interface GlobalModelState {
  collapsed: boolean;
}

export const openNotificationWithIcon = (type, msg) => {
  notification[type]({
    message: msg,
    description:
      'This is the content of the notification. This is the content of the notification. This is the content of the notification.',
  });
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
