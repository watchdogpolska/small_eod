import { fetchAll, fetchPage, create } from '@/services/tags';
import { Effect } from 'dva';
import { Reducer } from 'redux';
import { router } from 'umi';
import { Tag } from '@/services/definitions';
import { openNotificationWithIcon } from '@/models/global';
import { formatMessage } from 'umi-plugin-react/locale';

export type TagDefaultState = Tag[];

export interface TagModelType {
  namespace: string;
  state: Tag[];
  effects: {
    create: Effect;
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
    *create({ payload }, { call }) {
      try {
        const response = yield call(create, payload);
        openNotificationWithIcon(
          'success',
          formatMessage({ id: 'tags-new.page-create-notiffy-success' }) + response.data.id,
        );
        router.replace(`/tags/list`);
      } catch (err) {
        if (err.response.status === 400 && err.response.body.name) {
          err.response.body.name.forEach(message =>
            openNotificationWithIcon(
              'error',
              formatMessage({ id: 'tags-new.page-create-notiffy-error' }) + message,
            ),
          );
        } else {
          openNotificationWithIcon(
            'error',
            formatMessage({ id: 'tags-new.page-create-notiffy-error' }) + err.response.body.detail,
          );
        }
      }
    },
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
