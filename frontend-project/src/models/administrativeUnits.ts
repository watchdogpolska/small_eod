import { fetchAll, fetchOne } from '@/services/administrativeUnits';
import { Effect } from 'dva';
import { AnyAction, Reducer } from 'redux';
import { AdministrativeUnit } from '@/services/definitions';

export type AdministrativeUnitsModelState = AdministrativeUnit[];

const defaultAdministrativeUnitsState: AdministrativeUnitsModelState = [];

export interface AdministrativeUnitModelType {
  namespace: string;
  state: AdministrativeUnitsModelState;
  effects: {
    fetchAll: Effect;
    fetchOne: Effect;
  };
  reducers: {
    saveAll: Reducer<AdministrativeUnitsModelState, AnyAction>;
    saveOne: Reducer<AdministrativeUnitsModelState, AnyAction>;
  };
}

const AdministrativeUnitsModel: AdministrativeUnitModelType = {
  namespace: 'administrativeUnits',
  state: defaultAdministrativeUnitsState,
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

export default AdministrativeUnitsModel;
