import { fetchPage, fetchOne, Channel } from '@/services/channels';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';

export interface ChannelModelType {
  namespace: string;
  state: Channel[];
  effects: {
    fetchPage: Effect;
    fetchOne: Effect;
  };
  reducers: {
    savePage: Reducer<Channel[], AnyAction>;
    saveOne: Reducer<Channel[], AnyAction>;
  };
}
const defaultChannelsState: Channel[] = [];

const ChannelsModel: ChannelModelType = {
  namespace: 'channels',
  state: defaultChannelsState,
  effects: {
    *fetchPage({ payload }: AnyAction, { call, put }: EffectsCommandMap) {
      const response = yield call(fetchPage, payload);
      yield put({
        type: 'savePage',
        payload: response,
      });
      return response;
    },
    *fetchOne({ payload }: AnyAction, { call, put }: EffectsCommandMap) {
      const response = yield call(fetchOne, payload);
      yield put({
        type: 'saveOne',
        payload: response,
      });
    },
  },
  reducers: {
    savePage(_, { payload }) {
      return payload.data;
    },
    saveOne(state, { payload }) {
      return state.find(value => value.id === payload.id) ? state : [...state, payload];
    },
  },
};
export default ChannelsModel;
