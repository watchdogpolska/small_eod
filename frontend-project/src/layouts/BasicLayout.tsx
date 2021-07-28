import ProLayout, {
  BasicLayoutProps as ProLayoutProps,
  MenuDataItem,
  Settings,
} from '@ant-design/pro-layout';
import { Button, Result } from 'antd';
import { connect } from 'dva';
import React, { FC, useEffect } from 'react';
import { Dispatch } from 'redux';
import { Link, Redirect } from 'umi';
import { formatMessage } from 'umi-plugin-react/locale';
import logo from '../assets/logo.png';
import DefaultFooter from '../components/GlobalFooter/DefaultFooter';
import RightContent from '../components/GlobalHeader/RightContent';
import { useAuth } from '../hooks/useAuth';
import { ConnectState } from '../models/connect';
import Authorized from '../utils/Authorized';
import { getAuthorityFromRouter } from '../utils/utils';

const noMatch = (
  <Result
    status={403}
    title="403"
    subTitle="Sorry, you are not authorized to access this page."
    extra={
      <Button type="primary">
        <Link to="/login/sign-in">Go Login</Link>
      </Button>
    }
  />
);

export interface BasicLayoutProps extends ProLayoutProps {
  breadcrumbNameMap: {
    [path: string]: MenuDataItem;
  };
  route: ProLayoutProps['route'] & {
    authority: string[];
  };
  settings: Settings;
  dispatch: Dispatch;
}
export type BasicLayoutContext = { [K in 'location']: BasicLayoutProps[K] } & {
  breadcrumbNameMap: {
    [path: string]: MenuDataItem;
  };
};
/**
 * use Authorized check all menu item
 */

const menuDataRender = (menuList: MenuDataItem[]): MenuDataItem[] =>
  menuList.map(item => {
    const localItem = { ...item, children: item.children ? menuDataRender(item.children) : [] };
    return Authorized.check(item.authority, localItem, null) as MenuDataItem;
  });

const BasicLayout: FC<BasicLayoutProps> = props => {
  const {
    dispatch,
    children,
    settings,
    location = {
      pathname: '/',
    },
  } = props;
  const auth = useAuth();

  useEffect(() => {
    if (auth.isLoggedIn()) {
      auth.refreshToken();
      window.setInterval(() => auth.refreshToken(), ((auth.expires() * 1000) / 3) * 2);
    }
  }, []);

  const handleMenuCollapse = (payload: boolean): void => {
    if (dispatch) {
      dispatch({
        type: 'global/changeLayoutCollapsed',
        payload,
      });
    }
  };

  const authorized = getAuthorityFromRouter(props.route.routes, location.pathname || '/') || {
    authority: undefined,
  };

  if (!auth.isLoggedIn()) return <Redirect to="/login/sign-in" />;

  return (
    <>
      <ProLayout
        logo={logo}
        formatMessage={formatMessage}
        menuHeaderRender={(logoDom, titleDom) => (
          <Link to="/">
            {logoDom}
            {titleDom}
          </Link>
        )}
        onCollapse={handleMenuCollapse}
        menuItemRender={(menuItemProps, defaultDom) => {
          if (menuItemProps.isUrl || menuItemProps.children || !menuItemProps.path) {
            return defaultDom;
          }

          return <Link to={menuItemProps.path}>{defaultDom}</Link>;
        }}
        breadcrumbRender={(routers = []) => [
          {
            path: '/',
            breadcrumbName: formatMessage({
              id: 'menu.home',
            }),
          },
          ...routers,
        ]}
        itemRender={(route, _, routes) => {
          const lastBreadcrumbItem = routes.indexOf(route) === routes.length - 1;
          return !lastBreadcrumbItem ? (
            <Link to={route.path}>{route.breadcrumbName}</Link>
          ) : (
            <span>{route.breadcrumbName}</span>
          );
        }}
        footerRender={() => <DefaultFooter />}
        menuDataRender={menuDataRender}
        rightContentRender={() => <RightContent />}
        {...props}
        {...settings}
      >
        <Authorized authority={authorized!.authority} noMatch={noMatch}>
          {children}
        </Authorized>
      </ProLayout>
    </>
  );
};

export default connect(({ global, settings }: ConnectState) => ({
  collapsed: global.collapsed,
  settings,
}))(BasicLayout);
