import { fetchAll } from '@/services/users';

const UsersModel = {
  namespace: 'users',
  state: [],
  effects: {
    *fetchAll(_, { call, put }) {
      const response = yield call(fetchAll);
      yield put({
        type: 'saveAll',
        payload: response,
      });
    },
  },
  reducers: {
    saveAll(_, { payload }) {
      return payload.results;
    },
  },
};
export default UsersModel;
