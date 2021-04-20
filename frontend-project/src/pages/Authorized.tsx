import React, { ReactNode } from 'react';
import { Redirect } from 'umi';
import Authorized from '@/utils/Authorized';
import { getRouteAuthority } from '@/utils/utils';
import { Route } from '@/models/connect';
import { useAuth } from '@/hooks/useAuth';

interface AuthComponentProps {
  children: ReactNode;
  route: Route;
}

export default function AuthComponent({
  children,
  route = {
    routes: [],
  },
}: AuthComponentProps) {
  const auth = useAuth();
  const { routes = [] } = route;
  const isLogin = auth.isLoggedIn();
  return (
    <Authorized
      authority={getRouteAuthority(window.location.pathname, routes) || ''}
      noMatch={isLogin ? <Redirect to="/exception/403" /> : <Redirect to="/login/sign-in" />}
    >
      {children}
    </Authorized>
  );
}
