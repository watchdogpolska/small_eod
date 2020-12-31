import { PaginationParams, PaginationResponse } from '@/services/common';
import { Effect, EffectsCommandMap } from 'dva';
import { AnyAction, Reducer } from 'redux';
import {
  PostData,
  ReadOnlyServiceType,
  ReadWriteServiceType,
  ServiceResponse,
} from '../services/service';

interface Payload<T> extends AnyAction {
  payload: T;
}
interface PayloadWithCallback<T> extends Payload<T> {
  payload: T & { onResponse?: (props: ServiceResponse<T>) => void };
}

export type ReduxResourceState<T> = {
  data: Array<T>;
  isLoading: boolean;
  activeIO: number;
};

export type Resource = { id: number };

export type ReadOnlyReduxResourceT<T> = {
  namespace: string;
  state: ReduxResourceState<T>;
  effects: {
    fetchAll: Effect;
    fetchPage: Effect;
    fetchOne: Effect;
  };
  reducers: {
    incrementIO: Reducer<ReduxResourceState<T>, AnyAction>;
    decrementIO: Reducer<ReduxResourceState<T>, AnyAction>;
    saveAll: Reducer<ReduxResourceState<T>, Payload<ServiceResponse<Array<T>>>>;
    savePage: Reducer<ReduxResourceState<T>, Payload<ServiceResponse<PaginationResponse<T>>>>;
    saveOne: Reducer<ReduxResourceState<T>, Payload<ServiceResponse<T>>>;
  };
};

export type ReadWriteReduxResourceT<T> = {
  namespace: string;
  state: ReduxResourceState<T>;
  effects: ReadOnlyReduxResourceT<T>['effects'] & {
    create: Effect;
    update: Effect;
    remove: Effect;
  };
  reducers: ReadOnlyReduxResourceT<T>['reducers'] & {
    addOne: Reducer<ReduxResourceState<T>, Payload<ServiceResponse<T>>>;
    updateOne: Reducer<ReduxResourceState<T>, Payload<ServiceResponse<T>>>;
    removeOne: Reducer<ReduxResourceState<T>, Payload<ServiceResponse<number>>>;
  };
};

export function ReadOnlyReduxResource<T extends Resource>(props: {
  namespace: string;
  service: ReadOnlyServiceType<T>;
}): ReadOnlyReduxResourceT<T> {
  return {
    namespace: props.namespace,
    state: {
      data: new Array<T>(),
      isLoading: false,
      activeIO: 0,
    },
    effects: {
      *fetchAll(data: PayloadWithCallback<{}> | undefined, { call, put }: EffectsCommandMap) {
        yield put({ type: 'incrementIO' });
        const response = yield call(props.service.fetchAll);
        yield put({
          type: 'saveAll',
          payload: response,
        });
        yield put({ type: 'decrementIO' });
        yield data?.payload?.onResponse && call(data.payload.onResponse, response);
      },
      *fetchPage(
        { payload }: PayloadWithCallback<PaginationParams>,
        { call, put }: EffectsCommandMap,
      ) {
        yield put({ type: 'incrementIO' });
        const response = yield call(props.service.fetchPage, payload);
        yield put({
          type: 'savePage',
          payload: response,
        });
        yield put({ type: 'decrementIO' });
        yield payload.onResponse && call(payload.onResponse, response);
      },
      *fetchOne(
        { payload }: PayloadWithCallback<{ id: number }>,
        { call, put }: EffectsCommandMap,
      ) {
        yield put({ type: 'incrementIO' });
        const response = yield call(props.service.fetchOne, payload.id);
        yield put({
          type: 'saveOne',
          payload: response,
        });
        yield put({ type: 'decrementIO' });
        yield payload.onResponse && call(payload.onResponse, response);
      },
    },
    reducers: {
      incrementIO(state): ReduxResourceState<T> {
        return {
          ...state,
          activeIO: state.activeIO + 1,
          isLoading: true,
        };
      },
      decrementIO(state): ReduxResourceState<T> {
        return {
          ...state,
          activeIO: state.activeIO - 1,
          isLoading: state.activeIO - 1 !== 0,
        };
      },
      saveAll(state, { payload }): ReduxResourceState<T> {
        if (payload.status === 'failed') return state;

        return {
          ...state,
          data: payload.data,
        };
      },
      savePage(state, { payload }): ReduxResourceState<T> {
        if (payload.status === 'failed') return state;

        const newData = new Map<number, T>([
          ...state.data.map<[number, T]>(item => [item.id, item]),
          ...payload.data.data.map<[number, T]>(item => [item.id, item]),
        ]);

        return {
          ...state,
          data: Array.from(newData.values()),
        };
      },
      saveOne(state, { payload }): ReduxResourceState<T> {
        if (payload.status === 'failed') return state;

        const newData = new Map<number, T>([
          ...state.data.map<[number, T]>(item => [item.id, item]),
          [payload.data.id, payload.data],
        ]);

        return {
          ...state,
          data: Array.from(newData.values()),
        };
      },
    },
  };
}

export function ReadWriteReduxResource<T extends Resource>(props: {
  namespace: string;
  service: ReadWriteServiceType<T>;
}): ReadWriteReduxResourceT<T> {
  const readOnlyReduxResource = ReadOnlyReduxResource(props);

  return {
    namespace: props.namespace,
    state: {
      data: new Array<T>(),
      isLoading: false,
      activeIO: 0,
    },
    effects: {
      ...readOnlyReduxResource.effects,
      *create({ payload }: PayloadWithCallback<PostData<T>>, { call, put }: EffectsCommandMap) {
        yield put({ type: 'incrementIO' });
        const response = yield call(props.service.create, payload);
        yield put({
          type: 'createOne',
          payload: response,
        });
        yield put({ type: 'decrementIO' });
        yield payload.onResponse && call(payload.onResponse, response);
      },
      *update({ payload }: PayloadWithCallback<T>, { call, put }: EffectsCommandMap) {
        yield put({ type: 'incrementIO' });
        const response = yield call(props.service.update, payload);
        yield put({
          type: 'updateOne',
          payload: response,
        });
        yield put({ type: 'decrementIO' });
        yield payload.onResponse && call(payload.onResponse, response);
      },
      *remove({ payload }: PayloadWithCallback<{ id: number }>, { call, put }: EffectsCommandMap) {
        yield put({ type: 'incrementIO' });
        const response = yield call(props.service.remove, payload.id);
        yield put({
          type: 'removeOne',
          payload: response,
        });
        yield put({ type: 'decrementIO' });
        yield payload.onResponse && call(payload.onResponse, response);
      },
    },
    reducers: {
      ...readOnlyReduxResource.reducers,
      addOne(state, { payload }): ReduxResourceState<T> {
        if (payload.status === 'failed') return state;
        return {
          ...state,
          data: [...state.data, payload.data],
        };
      },
      updateOne(state, { payload }): ReduxResourceState<T> {
        if (payload.status === 'failed') return state;

        const newData = new Map<number, T>([
          ...state.data.map<[number, T]>(item => [item.id, item]),
          [payload.data.id, payload.data],
        ]);

        return {
          ...state,
          data: Array.from(newData.values()),
        };
      },
      removeOne(state, { payload }): ReduxResourceState<T> {
        if (payload.status === 'failed') return state;

        return {
          ...state,
          data: state.data.filter(item => item.id !== payload.data),
        };
      },
    },
  };
}
