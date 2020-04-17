import { fetchAll } from '@/services/tags';

export interface Tag {} // idk what properties Tag should have cuz its not mine code

export interface TagsState {
  tags: Tag[];
}

export interface TagsModelType {
  namespace: string;
  state: TagsState;
  effects: {
    fetchAll: any;
  };
  reducers: {
    saveAll: any;
  };
}

const defaultTagsState: TagsState = {
  tags: [],
};

const TagsModel = {
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
  },
  reducers: {
    saveAll(_, { payload }) {
      return payload.results;
    },
  },
};
export default TagsModel;
