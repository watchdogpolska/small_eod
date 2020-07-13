import { fetchOne } from '@/services/channels';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';

export interface Channel {
  id: number;
  name: string;
  city: boolean;
  voivodeship: boolean;
  flatNo: boolean;
  street: boolean;
  postalCode: boolean;
  houseNo: boolean;
  email: boolean;
  epuap: boolean;
}

export interface ChannelModelType {
  namespace: string;
  state: Channel[];
  effects: {
    fetchOne: Effect;
  };
  reducers: {
    saveOne: Reducer<Channel[], AnyAction>;
  };
}
const defaultChannelsState: Channel[] = [];

const InstitutionsModel: ChannelModelType = {
  namespace: 'channels',
  state: defaultChannelsState,
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
export default InstitutionsModel;
