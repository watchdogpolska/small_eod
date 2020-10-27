import { create } from '@/services/tags';
import { Effect } from 'dva';
import { Reducer } from 'redux';
import { router } from 'umi';
import { openNotificationWithIcon } from '@/models/global';
import { formatMessage } from 'umi-plugin-react/locale';
import { Tag } from '@/services/definitions';

export interface TagModelState {
  status?: number;
  tag?: Tag;
}

export interface TagModelType {
  namespace: string;
  state: TagModelState;
  effects: {
    create: Effect;
  };
  reducers: {
    changeTagStatus: Reducer<TagModelState>;
  };
}
const TagState: TagModelState = { status: 1, tag: { name: '', id: 0 } };
const TagModel: TagModelType = {
  namespace: 'tag',
  state: TagState,
  effects: {
    *create({ payload }, { call, put }) {
      try {
        const response = yield call(create, payload);
        yield put({
          type: 'changeTagStatus',
          payload: response,
        });
        openNotificationWithIcon(
          'success',
          formatMessage({ id: 'tags-new.page-create-notiffy-success' }) + response.data.id,
        );
        router.replace(`/tags/list`);
      } catch (err) {
        yield put({
          type: 'changeTagStatus',
          payload: err,
        });
      }
    },
  },
  reducers: {
    changeTagStatus(state, { payload }) {
      return {
        ...state,
        status: payload.response.status,
        tag: payload.response.body,
      };
    },
  },
};
export default TagModel;
