import { parse } from 'querystring';
import pathRegexp from 'path-to-regexp';
import { Route } from '@/models/connect';
import { Modal, notification } from 'antd';
import { IconType } from 'antd/lib/notification';
import { formatMessage } from 'umi-plugin-locale';
import { localeKeys } from '@/locales/pl-PL';
import React from 'react';

/* eslint no-useless-escape:0 import/prefer-default-export:0 */
const reg = /(((^https?:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+(?::\d+)?|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)$/;

export const isUrl = (path: string): boolean => reg.test(path);

export const getPageQuery = () => parse(window.location.href.split('?')[1]);

export const getAuthorityFromRouter = <T extends Route>(
  router: T[] = [],
  pathname: string,
): T | undefined => {
  const authority = router.find(
    ({ routes, path = '/' }) =>
      (path && pathRegexp(path).exec(pathname)) ||
      (routes && getAuthorityFromRouter(routes, pathname)),
  );
  if (authority) return authority;
  return undefined;
};

export const getRouteAuthority = (path: string, routeData: Route[]) => {
  let authorities: string[] | string | undefined;
  routeData.forEach(route => {
    // match prefix
    if (pathRegexp(`${route.path}/(.*)`).test(`${path}/`)) {
      if (route.authority) {
        authorities = route.authority;
      }
      // exact match
      if (route.path === path) {
        authorities = route.authority || authorities;
      }
      // get children authority recursively
      if (route.routes) {
        authorities = getRouteAuthority(path, route.routes) || authorities;
      }
    }
  });
  return authorities;
};

export function openNotificationWithIcon(message: IconType, title: string, description: string) {
  notification[message]({ message: title, description });
}

export function openRemoveConfirmationModal(
  name: string,
  onOk: () => void | Promise<void>,
  onCancel?: () => void | Promise<void>,
) {
  Modal.confirm({
    title: formatMessage({ id: localeKeys.modal.title }, { name }),
    content: <p>{formatMessage({ id: localeKeys.modal.description })}</p>,
    okText: formatMessage({ id: localeKeys.modal.confirm }),
    onOk,
    cancelText: formatMessage({ id: localeKeys.modal.cancel }),
    onCancel: () => onCancel && onCancel(),
  });
}
