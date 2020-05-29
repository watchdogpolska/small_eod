import { message } from 'antd';
import { routerRedux } from 'dva/router';
import { getPageQuery, setAuthority } from '@/utils/authority';
import { fakeAccountLogin, getFakeCaptcha } from '@/services/login';

const checkIfObjectIsArrayOfStrings = (obj: unknown): boolean => {
  if (Object.prototype.toString.call(obj) !== '[object Array]') {
    return false;
  }

  const arr = obj as Array<unknown>;

  if (arr.length < 1) {
    return false;
  }

  return arr.every((val: unknown) => {
    return typeof val === 'string';
  });
};

const Model = {
  namespace: 'userAndlogin',
  state: {
    status: undefined,
  },
  effects: {
    *login({ payload }, { call, put }) {
      const response = yield call(fakeAccountLogin, payload);
      yield put({
        type: 'changeLoginStatus',
        payload: response,
      }); // Login successfully

      if (response.status === 'ok') {
        message.success('Logged in successfully！');
        const urlParams = new URL(window.location.href);
        const params = getPageQuery();
        let { redirect } = params;

        if (checkIfObjectIsArrayOfStrings(redirect)) {
          redirect = (redirect as string[]).join('');
        }

        if (redirect) {
          const redirectUrlParams = new URL(redirect);

          if (redirectUrlParams.origin === urlParams.origin) {
            redirect = redirect.substr(urlParams.origin.length);

            if (redirect.match(/^\/.*#/)) {
              redirect = redirect.substr(redirect.indexOf('#') + 1);
            }
          } else {
            window.location.href = redirect;
            return;
          }
        }

        yield put(routerRedux.replace(redirect || '/'));
      }
    },

    *getCaptcha({ payload }, { call }) {
      yield call(getFakeCaptcha, payload);
    },
  },
  reducers: {
    changeLoginStatus(state, { payload }) {
      setAuthority(payload.currentAuthority);
      return { ...state, status: payload.status, type: payload.type };
    },
  },
};

export default Model;
