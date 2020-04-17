import { fetchAll } from '@/services/tags';

export interface TagsModelType {
  namespace: string;
  state: any[];
  effects: {
    fetchAll(
      _: any,
      {
        call,
        put,
      }: {
        call: any;
        put: any;
      },
    ): Generator<any, void, unknown>;
  };
  reducers: {
    saveAll(
      _: any,
      {
        payload,
      }: {
        payload: any;
      },
    ): any;
  };
}

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
