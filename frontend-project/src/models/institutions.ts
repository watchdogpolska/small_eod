import { fetchAll } from '@/services/institutions';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';

export interface Institution {
  id: number;
  name: string;
  email?: string;
  city?: string;
  epuap?: string;
  street?: string;
  houseNumber?: string;
  postalCode?: string;
  flatNumber?: string;
  NIP?: number;
  regon?: number;
}

export interface InstitutionModelType {
  namespace: string;
  state: Institution[];
  effects: {
    fetchAll: Effect;
  };
  reducers: {
    saveAll: Reducer<Institution[], AnyAction>;
  };
}
const defaultInstitutionsState: Institution[] = [];

const InstitutionsModel: InstitutionModelType = {
  namespace: 'institutions',
  state: defaultInstitutionsState,
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
export default InstitutionsModel;
