import { localeKeys } from '@/locales/pl-PL';
import { openNotificationWithIcon } from '@/models/global';
import { PaginationParams, PaginationResponse } from '@/services/common.d';
import { formatMessage } from 'umi-plugin-react/locale';

const DEFAULT_FECTH_PAGE_SIZE = 20;

export type Resource<T> = { id: T };
export type ResourceWithId = Resource<string> | Resource<number>;

type APIResponse<T> = {
  count: number;
  next: string;
  previous: string;
  results: Array<T>;
};

type PageQueryType = {
  query?: string;
  ordering?: string;
  limit?: number;
  offset?: number;
};

type PartialPick<T, K extends keyof T> = {
  [P in K]?: T[P];
};

export type PostData<T extends ResourceWithId> = PartialPick<T, 'id'>;

type ReadOnlyErrorTranslations = {
  fetchFailed: string;
};

type ReadWriteErrorTranslations = ReadOnlyErrorTranslations & {
  removeFailed: string;
  updateFailed: string;
  createFailed: string;
};

export type ReadOnlyServiceType<
  TList extends ResourceWithId,
  TDetail extends ResourceWithId = TList
> = {
  fetchPage: (props: PaginationParams) => Promise<PaginationResponse<TList>>;
  fetchOne: (id: TDetail['id']) => Promise<TDetail>;
};

export type ReadWriteServiceType<
  TList extends ResourceWithId,
  TDetail extends ResourceWithId = TList
> = ReadOnlyServiceType<TList, TDetail> & {
  create: (data: PostData<TDetail>) => Promise<TDetail>;
  update: (data: TDetail) => Promise<TDetail>;
  remove: (id: TDetail['id']) => Promise<TDetail['id']>;
};

async function handleError<T>(promise: Promise<T>, errorId: string) {
  try {
    return await promise;
  } catch (error: any) {
    openNotificationWithIcon(
      'error',
      formatMessage({ id: localeKeys.error }),
      formatMessage({ id: errorId }),
    );
    throw error;
  }
}

export function ReadOnlyService<
  TList extends ResourceWithId,
  TDetail extends ResourceWithId = TList
>(props: {
  readPage: (props: PageQueryType) => Promise<APIResponse<TList>>;
  readOne: (id: TDetail['id']) => Promise<TDetail>;
  translations: ReadOnlyErrorTranslations;
}): ReadOnlyServiceType<TList, TDetail> {
  function fetchPage(pageProps: PaginationParams): Promise<PaginationResponse<TList>> {
    return handleError(
      props
        .readPage({
          ...pageProps,
          limit: pageProps.pageSize || DEFAULT_FECTH_PAGE_SIZE,
          offset: pageProps.current ? pageProps.pageSize * (pageProps.current - 1) : 0,
        })
        .then(response => ({
          data: response.results,
          total: response.count,
        })),
      props.translations.fetchFailed,
    );
  }

  async function fetchOne(id: TDetail['id']): Promise<TDetail> {
    return handleError(props.readOne(id), props.translations.fetchFailed);
  }

  return {
    fetchPage,
    fetchOne,
  };
}

export function ReadWriteService<
  TList extends ResourceWithId,
  TDetail extends ResourceWithId = TList
>(props: {
  readPage: (props: PageQueryType) => Promise<APIResponse<TList>>;
  readOne: (id: TDetail['id']) => Promise<TDetail>;
  create: (data: PostData<TDetail>) => Promise<TDetail>;
  update: (id: TDetail['id'], data: TDetail) => Promise<TDetail>;
  remove: (id: TDetail['id']) => Promise<null>;
  translations: ReadWriteErrorTranslations;
}): ReadWriteServiceType<TList, TDetail> {
  function create(data: PostData<TDetail>): Promise<TDetail> {
    return handleError(props.create(data), props.translations.createFailed);
  }

  function update(data: TDetail): Promise<TDetail> {
    return handleError(props.update(data.id, data), props.translations.updateFailed);
  }

  function remove(id: TDetail['id']): Promise<TDetail['id']> {
    return handleError(
      props.remove(id).then(() => id),
      props.translations.removeFailed,
    );
  }

  return {
    ...ReadOnlyService(props),
    create,
    update,
    remove,
  };
}
