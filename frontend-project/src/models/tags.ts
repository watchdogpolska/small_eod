import { fetchAll, fetchPage } from '@/services/tags';
import { Effect } from 'dva';
import { Reducer } from 'redux';
import { Tag } from '@/services/swagger';

export type TagDefaultState = Tag[];

export interface TagModelType {
  namespace: string;
  state: Tag[];
  effects: {
    fetchAll: Effect;
    fetchPage: Effect;
  };
  reducers: {
    saveAll: Reducer<TagDefaultState>;
    savePage: Reducer<TagDefaultState>;
  };
}
const defaultTagsState: TagDefaultState = [];

const TagsModel: TagModelType = {
  namespace: 'tags',
  state: defaultTagsState,
  effects: {
    *fetchAll(_, { call, put }) {
      const response = yield call(fetchAll);
      yield put({
        type: 'saveAll',
        payload: response,
      });
    },
    *fetchPage({ payload }, { call, put }) {
      const response = yield call(fetchPage, payload);
      yield put({
        type: 'savePage',
        payload: response,
      });
      return response;
    },
  },
  reducers: {
    saveAll(_, { payload }) {
      return payload.results;
    },
    savePage(_, { payload }) {
      return payload.data;
    },
  },
};
export default TagsModel;
