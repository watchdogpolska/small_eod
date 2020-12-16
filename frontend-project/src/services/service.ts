import { PaginationParams, PaginationResponse } from '@/services/common.d';
import { Resource } from '../utils/reduxModel';

const FECTH_ALL_PAGE_SIZE = 20;

type APIResponse<T> = {
  count: number;
  next: string;
  previous: string;
  results: Array<T>;
};

type PageQueryType = {
  limit: number;
  offset: number;
};

type HttpInfo<T> = {
  data: T;
  response: Response;
};

export type PostData<T> = Omit<T, 'id'>;

export type ServiceResponse<T> =
  | {
      status: 'success';
      data: T;
      statusCode: number;
    }
  | {
      status: 'failed';
      statusCode: number;
      errorBody: any;
      errorText: string;
    };

export type ReadOnlyServiceType<T> = {
  fetchAll: () => Promise<ServiceResponse<Array<T>>>;
  fetchPage: (props: PaginationParams) => Promise<ServiceResponse<PaginationResponse<T>>>;
  fetchOne: (id: number) => Promise<ServiceResponse<T>>;
};

export type ReadWriteServiceType<T> = ReadOnlyServiceType<T> & {
  create: (data: PostData<T>) => Promise<ServiceResponse<T>>;
  update: (data: T) => Promise<ServiceResponse<T>>;
  remove: (id: number) => Promise<ServiceResponse<number>>;
};

function handleError<Y>(promise: Promise<HttpInfo<Y>>): Promise<ServiceResponse<Y>> {
  return promise.then(
    response => ({
      status: 'success',
      data: response.data,
      statusCode: response.response.status,
    }),
    error => ({
      status: 'failed',
      statusCode: error.status,
      errorBody: error.response?.body,
      errorText: error.response?.text,
    }),
  );
}

export function ReadOnlyService<T extends Resource>(props: {
  readPage: (props: PageQueryType) => Promise<HttpInfo<APIResponse<T>>>;
  readOne: (id: number) => Promise<HttpInfo<T>>;
}): ReadOnlyServiceType<T> {
  async function fetchAll(): Promise<ServiceResponse<Array<T>>> {
    const firstResponse = await fetchPage({ current: 1, pageSize: FECTH_ALL_PAGE_SIZE });
    if (firstResponse.status === 'failed') return firstResponse;

    const numberOfPagesToFetch = Math.ceil(firstResponse.data.total / FECTH_ALL_PAGE_SIZE) - 1;
    const pagePromises = new Array(numberOfPagesToFetch)
      .fill(undefined)
      .map((_, idx) => fetchPage({ current: idx + 2, pageSize: FECTH_ALL_PAGE_SIZE }));
    const otherResponses = await Promise.all(pagePromises);
    const failedReponse = otherResponses.find(response => response.status === 'failed');
    if (failedReponse) return failedReponse as any;

    return {
      status: 'success',
      statusCode: firstResponse.statusCode,
      data: [firstResponse, ...otherResponses].reduce(
        (acc, response) => [...acc, ...(response.status === 'success' ? response.data.data : [])],
        new Array<T>(),
      ),
    };
  }

  async function fetchPage({
    current,
    pageSize,
  }: PaginationParams): Promise<ServiceResponse<PaginationResponse<T>>> {
    const response = await handleError(
      props.readPage({
        limit: pageSize,
        offset: pageSize * (current - 1),
      }),
    );
    if (response.status === 'failed') return response;
    return {
      status: 'success',
      statusCode: response.statusCode,
      data: {
        data: response.data.results,
        total: response.data.count,
      },
    };
  }

  function fetchOne(id: number): Promise<ServiceResponse<T>> {
    return handleError(props.readOne(id));
  }

  return {
    fetchAll,
    fetchPage,
    fetchOne,
  };
}

export function ReadWriteService<T extends Resource>(props: {
  readPage: (props: PageQueryType) => Promise<HttpInfo<APIResponse<T>>>;
  readOne: (id: number) => Promise<HttpInfo<T>>;
  create: (data: PostData<T>) => Promise<HttpInfo<T>>;
  update: (id: number, data: T) => Promise<HttpInfo<T>>;
  remove: (id: number) => Promise<HttpInfo<null>>;
}): ReadWriteServiceType<T> {
  function create(data: PostData<T>): Promise<ServiceResponse<T>> {
    return handleError(props.create(data));
  }

  function update(data: T): Promise<ServiceResponse<T>> {
    return handleError(props.update(data.id, data));
  }

  function remove(id: number): Promise<ServiceResponse<number>> {
    return handleError(props.remove(id)).then(
      suc => ({ ...suc, data: id }),
      err => err,
    );
  }

  return {
    ...ReadOnlyService(props),
    create,
    update,
    remove,
  };
}
