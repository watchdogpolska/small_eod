import { fetchAll, fetchOne } from '@/services/institutions';
import { Effect } from 'dva';
import { AnyAction, Reducer } from 'redux';
import { Institution } from '@/services/swagger';

export type InstitutionsModelState = Institution[];

const defaultInstitutionsState: InstitutionsModelState = [];

export interface InstitutionModelType {
  namespace: string;
  state: InstitutionsModelState;
  effects: {
    fetchAll: Effect;
    fetchOne: Effect;
  };
  reducers: {
    saveAll: Reducer<InstitutionsModelState, AnyAction>;
    saveOne: Reducer<InstitutionsModelState, AnyAction>;
  };
}

const InstitutionsModel: InstitutionModelType = {
  namespace: 'institutions',
  state: defaultInstitutionsState,
  effects: {
    *fetchAll(_, { call, put }) {
      const response = yield call(fetchAll);
      yield put({
        type: 'saveAll',
        payload: response,
      });
    },
    *fetchOne({ payload }, { call, put }) {
      const response = yield call(fetchOne, payload);
      yield put({
        type: 'saveOne',
        payload: response,
      });
    },
  },
  reducers: {
    saveAll(_, { payload }) {
      return payload.results;
    },
    saveOne(state, { payload }) {
      return state.find(value => value.id === payload.id) ? state : [...state, payload];
    },
  },
};
export default InstitutionsModel;
