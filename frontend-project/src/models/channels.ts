import { fetchPage, Channel } from '@/services/channels';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';

export interface ChannelModelType {
  namespace: string;
  state: { data: Channel[]; total: number };
  effects: {
    fetchPage: Effect;
  };
  reducers: {
    savePage: Reducer<Channel[], AnyAction>;
  };
}
const defaultChannelsState: { data: Channel[]; total: number } = { data: [], total: 0 };

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
  },
  reducers: {
    savePage(_, { payload }) {
      return payload;
    },
  },
};
export default ChannelsModel;
