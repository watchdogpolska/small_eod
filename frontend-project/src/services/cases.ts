import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';
import { Case } from '@/services/swagger';

export async function fetchCasesPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<Case>> {
  smallEodSDK.CasesApi();

  const sdkResponse = await smallEodSDK.casesList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}

export const fetchOne = async (id: number): Promise<Case> => {
  return new smallEodSDK.CasesApi().casesRead(id);
};
