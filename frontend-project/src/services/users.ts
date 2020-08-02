import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';

export interface User {
  username: string;
  email: string;
  firstName: string;
  lastName: string;
  id: number;
}

export interface Page {
  results: User[];
  count: number;
  next: string;
  previous: string;
}

function fetchAllPages(page: Page) {
  if (page.next) {
    const params = new URL(page.next).searchParams;
    return smallEodSDK
      .usersList({
        limit: params.get('limit'),
        offset: params.get('offset'),
      })
      .then(newPage => {
        const nextPage = newPage;
        nextPage.results = page.results.concat(nextPage.results);
        return fetchAllPages(nextPage);
      });
  }

  return page;
}

export async function fetchUsersPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<User>> {
  const sdkResponse = await new smallEodSDK.UsersApi().usersList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}

export async function fetchAll() {
  smallEodSDK.UsersApi();

  return smallEodSDK.usersList().then(page => fetchAllPages(page));
}
