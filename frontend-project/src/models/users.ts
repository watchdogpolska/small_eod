import { fetchAll } from '@/services/users';
import { Effect, EffectsCommandMap } from 'dva';
import { Reducer, AnyAction } from 'redux';

export interface User {
  username: string;
  email: string;
  firstName: string;
  lastName: string;
  id: number;
}

export interface UsersState {
  users: User[];
}

export interface UsersModelType {
  namespace: string;
  state: UsersState;
  effects: {
    fetchAll: Effect;
  };
  reducers: {
    saveAll: Reducer<UsersState>;
  };
}

const UsersModel = {
  namespace: 'users',
  state: [],
  effects: {
    *fetchAll(_: AnyAction, { call, put }: EffectsCommandMap) {
      const response = yield call(fetchAll);
      yield put({
        type: 'saveAll',
        payload: response,
      });
    },
  },
  reducers: {
    saveAll(_: AnyAction, { payload }: EffectsCommandMap) {
      return payload.results;
    },
  },
};
export default UsersModel;
