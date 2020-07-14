import { fetchPage, DocumentType } from '@/services/documentTypes';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';

export interface DocumentTypeModelType {
  namespace: string;
  state: DocumentType[];
  effects: {
    fetchPage: Effect;
  };
  reducers: {
    savePage: Reducer<DocumentType[], AnyAction>;
  };
}
const defaultDocumentTypesState: DocumentType[] = [];

const DocumentTypesModel: DocumentTypeModelType = {
  namespace: 'documentTypes',
  state: defaultDocumentTypesState,
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
      return payload.data;
    },
  },
};
export default DocumentTypesModel;
