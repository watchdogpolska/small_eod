import smallEodSDK from '@/utils/sdk';
import { PaginationParams, PaginationResponse } from '@/services/common.d';
import { AdministrativeUnit } from './definitions';

function fetchAllPages(page) {
  if (page.next) {
    const params = new URL(page.next).searchParams;
    return smallEodSDK
      .administrativeUnitsList({
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

export async function fetchAdministrativeUnitsPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<AdministrativeUnit>> {
  const sdkResponse = await new smallEodSDK.AdministrativeUnitsApi().administrativeUnitsList({
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
  return smallEodSDK.administrativeUnitsList().then(page => fetchAllPages(page));
}

export async function fetchOne(id: number): Promise<AdministrativeUnit> {
  return new smallEodSDK.AdministrativeUnitsApi().administrativeUnitsRead(id);
}
