export type PaginationParams = {
  query?: string;
  ordering?: string;
  current?: number;
  pageSize?: number;
};

export interface PaginationResponse<T> {
  data: T[];
  total: number;
}

export type OptionType<L = string, V = string> = {
  label: L;
  value: V;
};

export type KeysWithValsOfType<T, V> = { [K in keyof T]-?: T[K] extends V ? K : never }[keyof T];

export type Awaited<T> = T extends PromiseLike<infer U> ? Awaited<U> : T;
