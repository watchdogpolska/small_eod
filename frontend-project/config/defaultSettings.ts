import { MenuTheme } from 'antd/es/menu/MenuContext';

export type ContentWidth = 'Fluid' | 'Fixed';

export interface DefaultSettings {
  navTheme: MenuTheme;
  primaryColor: string;
  layout: 'sidemenu' | 'topmenu';
  contentWidth: ContentWidth;
  fixedHeader: boolean;
  autoHideHeader: boolean;
  fixSiderbar: boolean;
  menu: { locale: boolean };
  title: string;
  pwa: boolean;
  iconfontUrl: string;
  colorWeak: boolean;
}

export default {
  navTheme: 'dark',
  primaryColor: 'daybreak',
  layout: 'sidemenu',
  contentWidth: 'Fluid',
  fixedHeader: false,
  autoHideHeader: false,
  fixSiderbar: false,
  colorWeak: false,
  menu: {
    locale: true,
  },
  title: 'Ant Design Pro',
  pwa: false,
  iconfontUrl: '',
} as DefaultSettings;
