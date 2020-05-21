import request from '@/utils/request';

export const fakeAccountLogin = async (params: unknown) => {
  return request('/api/login/account', {
    method: 'POST',
    data: params,
  });
};

export const getFakeCaptcha = async (mobile: string) => {
  return request(`/api/login/captcha?mobile=${mobile}`);
};
