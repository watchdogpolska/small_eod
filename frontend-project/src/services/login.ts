import request from '@/utils/request';

export interface LoginParams {
  userName: string;
  password: string;
  mobile: string;
  captcha: string;
}

export interface FakeAccountLoginResponse {
  status: 'ok' | 'error';
  type: string;
  currentAuthority: string;
}

export const fakeAccountLogin = async (params: LoginParams): Promise<FakeAccountLoginResponse> => {
  return request('/api/login/account', {
    method: 'POST',
    data: params,
  });
};

export const getFakeCaptcha = async (mobile: string) => {
  return request(`/api/login/captcha?mobile=${mobile}`);
};
