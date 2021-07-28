import { GoogleOutlined } from '@ant-design/icons';
import { Button } from 'antd';
import React from 'react';
import { formatMessage } from 'umi-plugin-react/locale';
import { localeKeys } from '../../locales/pl-PL';
import { UsersService } from '../../services/users';
import styles from './sign-in.less';

export default function SignInView() {
  const { login } = localeKeys;
  function loginUsingGoogle() {
    UsersService.auth().then(request => {
      window.location.href = request.url;
    });
  }

  return (
    <div className={styles.main}>
      <Button icon={<GoogleOutlined />} onClick={loginUsingGoogle}>
        {formatMessage({ id: login.loginGoogle })}
      </Button>
    </div>
  );
}
