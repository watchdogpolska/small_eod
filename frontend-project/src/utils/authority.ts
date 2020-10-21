import QueryString, { parse } from 'qs';

export const getAuthority = (str?: string): string | string[] => {
  const authorityString =
    typeof str === 'undefined' && localStorage ? localStorage.getItem('antd-pro-authority') : str; // authorityString could be admin, "admin", ["admin"]

  let authority: string | string[];

  try {
    if (authorityString) {
      authority = JSON.parse(authorityString);
    }
  } catch (e) {
    authority = authorityString;
  }

  if (typeof authority === 'string') {
    return [authority];
  }

  return authority;
};

export const getPageQuery = (): QueryString.ParsedQs => {
  return parse(window.location.href.split('?')[1]);
};
