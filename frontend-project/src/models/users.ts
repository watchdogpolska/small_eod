import { fetchAll } from '@/services/users';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction } from 'redux';
import { Reducer } from 'react';

export interface User {
  username: string;
  email: string;
  firstName: string;
  lastName: string;
  id: number;
}

export interface Payload {
  payload: { results: User[] };
}

export interface UsersModelType {
  namespace: string;
  state: User[];
  effects: {
    fetchAll: Effect;
  };
  reducers: {
    saveAll: Reducer<User[], Payload>;
  };
}
const defaultUsersState: User[] = [];

const UsersModel: UsersModelType = {
  namespace: 'users',
  state: defaultUsersState,
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
    saveAll(_, { payload }) {
      return payload.results;
    },
  },
};
export default UsersModel;
