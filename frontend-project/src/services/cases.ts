import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';

export interface Case {
  name: string;
  audited_institutions: number;
  comment: string;
  tags: [number];
  responsible_users: [number];
  notified_users: [number];
  featureoptions: [number];
  createdBy: number;
  createdOn: string;
  id: number;
  modifiedBy: number;
  modifiedOn: string;
}

export async function fetchCasesPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<Case>> {
  smallEodSDK.CasesApi();

  const sdkResponse = await smallEodSDK.casesList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });
  sdkResponse.results = sdkResponse.results.map(item => ({
    ...item,
    createdOn: item.createdOn.toLocaleString(),
    modifiedOn: item.modifiedOn.toLocaleString(),
  }));

  console.log(sdkResponse.results[0].createdOn);
  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}
