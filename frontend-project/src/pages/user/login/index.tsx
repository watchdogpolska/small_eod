import { AlipayCircleOutlined, TaobaoCircleOutlined, WeiboCircleOutlined } from '@ant-design/icons';
import { Alert, Checkbox } from 'antd';
import React, { useState } from 'react';
import { connect } from 'dva';
import LoginFrom from '@/components/Login';
import { Dispatch } from 'redux';
import { LoginModelState, LoginModelType } from '@/models/login';
import { LoginParams } from '@/services/login';
import styles from './style.less';

const { Tab, UserName, Password, Submit } = LoginFrom;

export interface LoginMessageProps {
  content: string;
}

const LoginMessage = ({ content }: LoginMessageProps) => (
  <Alert
    style={{
      marginBottom: 24,
    }}
    message={content}
    type="error"
    showIcon
  />
);

export interface UserLoginProps {
  dispatch: Dispatch;
  submitting: boolean;
  userAndlogin: LoginModelState;
}

const UserLogin = (props: UserLoginProps) => {
  const { userAndlogin = {}, submitting } = props;
  const { status, type: loginType } = userAndlogin;
  const [autoLogin, setAutoLogin] = useState(true);
  const [type, setType] = useState('account');

  const handleSubmit = (values: LoginParams) => {
    const { dispatch } = props;
    dispatch({
      type: 'login/login',
      payload: { ...values, type },
    });
  };

  return (
    <div className={styles.main}>
      <LoginFrom activeKey={type} onTabChange={setType} onSubmit={handleSubmit}>
        <Tab key="account" tab="Hasło logowania do konta">
          {status === 'error' && loginType === 'account' && !submitting && (
            <LoginMessage content="Błąd konta lub hasła（admin/ant.design）" />
          )}

          <UserName
            name="userName"
            placeholder="Nazwa użytkownika: admin or user"
            rules={[
              {
                required: true,
                message: 'Proszę podać swoją nazwę użytkownika!',
              },
            ]}
          />
          <Password
            name="password"
            placeholder="Hasło: ant.design"
            rules={[
              {
                required: true,
                message: 'Proszę podać hasło!',
              },
            ]}
          />
        </Tab>
        <div>
          <Checkbox checked={autoLogin} onChange={e => setAutoLogin(e.target.checked)}>
            Zaloguj autmatycznie
          </Checkbox>
          {/* <a
            style={{
              float: 'right',
            }}
          ></a> */}
        </div>
        <Submit loading={submitting}>Submit</Submit>
        <div className={styles.other}>
          <AlipayCircleOutlined className={styles.icon} />
          <TaobaoCircleOutlined className={styles.icon} />
          <WeiboCircleOutlined className={styles.icon} />
        </div>
      </LoginFrom>
    </div>
  );
};

export interface LoginConnectProps {
  userAndlogin: LoginModelState;
  loading: LoginModelType;
}

export default connect(({ userAndlogin, loading }: LoginConnectProps) => ({
  state: userAndlogin,
  submitting: loading.effects['userAndlogin/login'],
}))(UserLogin);
