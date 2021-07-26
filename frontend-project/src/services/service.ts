import { localeKeys } from '@/locales/pl-PL';
import { openNotificationWithIcon } from '@/utils/utils';
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

export type ReadOnlyServiceType<T extends ResourceWithId> = {
  fetchPage: (props: PaginationParams) => Promise<PaginationResponse<T>>;
  fetchOne: (id: T['id']) => Promise<T>;
};

export type ReadWriteServiceType<T extends ResourceWithId> = ReadOnlyServiceType<T> & {
  create: (data: PostData<T>) => Promise<T>;
  update: (data: T) => Promise<T>;
  remove: (id: T['id']) => Promise<T['id']>;
};

export async function handleError<T>(promise: Promise<T>, errorId: string) {
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

export function ReadOnlyService<T extends ResourceWithId>(props: {
  readPage: (props: PageQueryType) => Promise<APIResponse<T>>;
  readOne: (id: T['id']) => Promise<T>;
  translations: ReadOnlyErrorTranslations;
}): ReadOnlyServiceType<T> {
  function fetchPage(pageProps: PaginationParams): Promise<PaginationResponse<T>> {
    return handleError(
      props
        .readPage({
          ...pageProps,
          query: !pageProps.query ? undefined : pageProps.query,
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

  async function fetchOne(id: T['id']): Promise<T> {
    return handleError(props.readOne(id), props.translations.fetchFailed);
  }

  return {
    fetchPage,
    fetchOne,
  };
}

export function ReadWriteService<T extends ResourceWithId>(props: {
  readPage: (props: PageQueryType) => Promise<APIResponse<T>>;
  readOne: (id: T['id']) => Promise<T>;
  create: (data: PostData<T>) => Promise<T>;
  update: (id: T['id'], data: T) => Promise<T>;
  remove: (id: T['id']) => Promise<null>;
  translations: ReadWriteErrorTranslations;
}): ReadWriteServiceType<T> {
  function create(data: PostData<T>): Promise<T> {
    return handleError(props.create(data), props.translations.createFailed);
  }

  function update(data: T): Promise<T> {
    return handleError(props.update(data.id, data), props.translations.updateFailed);
  }

  function remove(id: T['id']): Promise<T['id']> {
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
