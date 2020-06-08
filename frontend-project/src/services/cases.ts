import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';

export interface Case {
  name: string;
  auditedInstitutions: [number];
  comment: string;
  tags: [string];
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

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}
