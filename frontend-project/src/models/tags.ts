import { fetchAll } from '@/services/tags';
import { Effect, EffectsCommandMap } from 'dva';
import { Reducer, AnyAction } from 'redux';

export interface Tag {} // idk what properties Tag should have cuz its not mine code

export interface TagsState {
  tags: Tag[];
}

export interface TagsModelType {
  namespace: string;
  state: TagsState;
  effects: {
    fetchAll: Effect;
  };
  reducers: {
    saveAll: Reducer<TagsState>;
  };
}

const defaultTagsState: TagsState = {
  tags: [],
};

const TagsModel = {
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
  },
  reducers: {
    saveAll(_: AnyAction, { payload }: EffectsCommandMap) {
      return payload.results;
    },
  },
};
export default TagsModel;
