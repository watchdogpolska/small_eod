export interface PaginationParams {
  current: number;
  pageSize: number;
}

export interface PaginationResponse<T> {
  data: T[];
  total: number;
}
