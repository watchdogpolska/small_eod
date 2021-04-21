import { MenuDataItem } from '@ant-design/pro-layout';
import { RouterTypes } from 'umi/routerTypes';
import { GlobalModelState } from './global';
import { DefaultSettings as SettingModelState } from '../../config/defaultSettings';
import { UserModelState } from './user';
import { LoginModelState } from './login';

export { GlobalModelState, SettingModelState, UserModelState };

export interface Loading {
  global: boolean;
  effects: { [key: string]: boolean | undefined };
  models: {
    global?: boolean;
    menu?: boolean;
    setting?: boolean;
    user?: boolean;
    login?: boolean;
  };
}

export type ConnectState = {
  global: GlobalModelState;
  loading: Loading;
  userAndlogin: LoginModelState;
  settings: SettingModelState;
  user: UserModelState;
  login: LoginModelState;
};

export type DetailMatchParam = {
  match: RouterTypes['match'] & { params: { id: string | undefined } };
};

export interface Route extends MenuDataItem {
  routes?: Route[];
}
