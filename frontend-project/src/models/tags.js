import { fetchAll } from '@/services/tags';

const TagsModel = {
  namespace: 'tags',
  state: [],
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
