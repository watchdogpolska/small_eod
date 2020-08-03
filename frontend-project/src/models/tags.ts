import { fetchAll, fetchPage, Tag } from '@/services/tags';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';

export interface TagModelType {
  namespace: string;
  state: Tag[];
  effects: {
    fetchAll: Effect;
    fetchPage: Effect;
  };
  reducers: {
    saveAll: Reducer<Tag[], AnyAction>;
    savePage: Reducer<Tag[], AnyAction>;
  };
}
const defaultTagsState: Tag[] = [];

const TagsModel: TagModelType = {
  namespace: 'tags',
  state: defaultTagsState,
  effects: {
    *fetchAll(_: AnyAction, { call, put }: EffectsCommandMap) {
      const response = yield call(fetchAll);
      yield put({
        type: 'saveAll',
        payload: response,
      });
    },
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
    saveAll(_, { payload }) {
      return payload.results;
    },
    savePage(_, { payload }) {
      return payload.data;
    },
  },
};
export default TagsModel;
