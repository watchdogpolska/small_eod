import { notification } from 'antd';

export interface GlobalModelState {
  collapsed: boolean;
}

export const openNotificationWithIcon = (type, msg) => {
  notification[type]({
    message: msg,
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
