import { fetchOne } from '@/services/documentTypes';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';

export interface DocumentType {
  id: number;
  name: string;
}

export interface DocumentTypeModelType {
  namespace: string;
  state: DocumentType[];
  effects: {
    fetchOne: Effect;
  };
  reducers: {
    saveOne: Reducer<DocumentType[], AnyAction>;
  };
}
const defaultDocumentTypesState: DocumentType[] = [];

const DocumentTypesModel: DocumentTypeModelType = {
  namespace: 'documentTypes',
  state: defaultDocumentTypesState,
  effects: {
    *fetchOne({ payload }: AnyAction, { call, put }: EffectsCommandMap) {
      const response = yield call(fetchOne, payload);
      yield put({
        type: 'saveOne',
        payload: response,
      });
    },
  },
  reducers: {
    saveOne(state, { payload }) {
      return state.find(value => value.id === payload.id) ? state : [...state, payload];
    },
  },
};
export default DocumentTypesModel;
