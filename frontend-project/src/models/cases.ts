import { fetchOne } from '@/services/cases';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';
import { Case } from '@/services/swagger';

export type CaseModelState = Case[];

export interface CaseModelType {
  namespace: string;
  state: CaseModelState;
  effects: {
    fetchOne: Effect;
  };
  reducers: {
    saveOne: Reducer<CaseModelState, AnyAction>;
  };
}

const defaultCasesState: CaseModelState = [];

const CasesModel: CaseModelType = {
  namespace: 'cases',
  state: defaultCasesState,
  effects: {
    *fetchOne({ payload }: AnyAction, { call, put }: EffectsCommandMap) {
      const response = yield call(fetchOne, payload);
      yield put({
        type: 'saveOne',
        payload: response,
      });
    },
  },
  reducers: {
    saveOne(state, { payload }) {
      return state.find(value => value.id === payload.id) ? state : [...state, payload];
    },
  },
};
export default CasesModel;
