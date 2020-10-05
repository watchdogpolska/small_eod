import smallEodSDK from '@/utils/sdk';
import { PaginationParams, PaginationResponse } from '@/services/common.d';
import { Institution } from '@/services/swagger';

function fetchAllPages(page) {
  if (page.next) {
    const params = new URL(page.next).searchParams;
    return smallEodSDK
      .institutionsList({
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

export async function fetchInstitutionPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<Institution>> {
  const sdkResponse = await new smallEodSDK.InstitutionsApi().institutionsList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}

export async function fetchAll() {
  smallEodSDK.InstitutionsApi();
  return smallEodSDK.institutionsList().then(page => fetchAllPages(page));
}

export async function fetchOne(id: number) {
  return new smallEodSDK.InstitutionsApi().institutionsRead(id);
}
