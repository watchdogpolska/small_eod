import { Space, Spin } from 'antd';
import React, { useEffect } from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { useAuth } from '../../hooks/useAuth';
import { localeKeys } from '../../locales/pl-PL';
import { UsersService } from '../../services/users';
import styles from './sign-in.less';

export default function OAuthCallbackView() {
  const { login } = localeKeys;
  const auth = useAuth();
  useEffect(() => {
    const initialQueryParametrs = new URLSearchParams(window.location.search);
    const paramsArray: [string, string][] = [];
    initialQueryParametrs.forEach((value, key) => paramsArray.push([key, value]));
    const params = paramsArray.reduce((acc, [key, value]) => ({ ...acc, [key]: value }), {});
    UsersService.exchange(params)
      .then(response => {
        auth.setTokens(response);
        window.location.href = '/';
      })
      .catch(() => {
        window.location.href = '/login/sign-in';
      });
  }, []);

  return (
    <div className={styles.main}>
      <Space size="small">
        <span>{formatMessage({ id: login.authorization })}</span>
        <Spin />
      </Space>
    </div>
  );
}
