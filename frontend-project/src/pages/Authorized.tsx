import React, { FC } from 'react';
import { Redirect } from 'umi';
import Authorized from '@/utils/Authorized';
import { getRouteAuthority } from '@/utils/utils';
import { ConnectState, UserModelState, Route } from '@/models/connect';
import { connect } from 'dva';
import { useAuth } from '@/hooks/useAuth';

interface AuthComponentProps {
  user: UserModelState;
  route: Route;
  location: Location;
}

const AuthComponent: FC<AuthComponentProps> = ({
  children,
  route = {
    routes: [],
  },
  location = {
    pathname: '',
  },
}) => {
  const auth = useAuth();
  const { routes = [] } = route;
  const isLogin = auth.isLoggedIn();
  return (
    <Authorized
      authority={getRouteAuthority(location.pathname, routes) || ''}
      noMatch={isLogin ? <Redirect to="/exception/403" /> : <Redirect to="/login/sign-in" />}
    >
      {children}
    </Authorized>
  );
};

export default connect(({ user }: ConnectState) => ({
  user,
}))(AuthComponent);
