import { fetchPage, fetchOne } from '@/services/channels';
import { Effect } from 'dva';
import { AnyAction, Reducer } from 'redux';
import { Channel } from '@/services/definitions';

export type ChannelModelState = Channel[];

export interface ChannelModelType {
  namespace: string;
  state: ChannelModelState;
  effects: {
    fetchPage: Effect;
    fetchOne: Effect;
  };
  reducers: {
    savePage: Reducer<ChannelModelState, AnyAction>;
    saveOne: Reducer<ChannelModelState, AnyAction>;
  };
}

const defaultChannelsState: ChannelModelState = [];

const ChannelsModel: ChannelModelType = {
  namespace: 'channels',
  state: defaultChannelsState,
  effects: {
    *fetchPage({ payload }, { call, put }) {
      const response = yield call(fetchPage, payload);
      yield put({
        type: 'savePage',
        payload: response,
      });
      return response;
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
    savePage(_, { payload }) {
      return payload.data;
    },
    saveOne(state, { payload }) {
      return state.find(value => value.id === payload.id) ? state : [...state, payload];
    },
  },
};
export default ChannelsModel;
