import RenderAuthorize from '@/components/Authorized';
import { getAuthority } from './authority';
/* eslint-disable eslint-comments/disable-enable-pair */
/* eslint-disable import/no-mutable-exports */
let Authorized = RenderAuthorize(getAuthority());

// Reload the rights component
export const reloadAuthorized = (): void => {
  Authorized = RenderAuthorize(getAuthority());
};

export const setAuthority = (authority: string | string[]): void => {
  const proAuthority = typeof authority === 'string' ? [authority] : authority;
  localStorage.setItem('antd-pro-authority', JSON.stringify(proAuthority)); // auto reload

  reloadAuthorized();
};

/**
 * hard code
 * block need it。
 */
window.reloadAuthorized = reloadAuthorized;

export default Authorized;
