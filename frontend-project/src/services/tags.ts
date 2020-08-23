import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';

export interface Tag {
  name: string;
}
export interface Page {
  results: Tag[];
  count: number;
  next: string;
  previous: string;
}

function fetchAllPages(page: Page) {
  if (page.next) {
    const params = new URL(page.next).searchParams;
    return smallEodSDK
      .tagsList({
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

export async function fetchPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<Tag>> {
  const sdkResponse = await new smallEodSDK.TagsApi().tagsList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}

export async function fetchAll() {
  smallEodSDK.TagsApi();
  return smallEodSDK.tagsList().then(page => fetchAllPages(page));
}
