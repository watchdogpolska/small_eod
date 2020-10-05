import { fetchAll } from '@/services/users';
import { Effect } from 'dva';
import { Reducer } from 'react';
import { User } from '@/services/swagger';

export type UsersModelState = User[];

export interface SaveAllUsersPayload {
  payload: { results: User[] };
}

export interface UsersModelType {
  namespace: string;
  state: UsersModelState;
  effects: {
    fetchAll: Effect;
  };
  reducers: {
    saveAll: Reducer<UsersModelState, SaveAllUsersPayload>;
  };
}

const defaultUsersState: User[] = [];

const UsersModel: UsersModelType = {
  namespace: 'users',
  state: defaultUsersState,
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
