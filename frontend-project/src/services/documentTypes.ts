import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';

export interface DocumentType {
  name: string;
}

export async function fetchDocumentTypesPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<DocumentType>> {
  const sdkResponse = await new smallEodSDK.DocumentTypesApi().documentTypesList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}

export const fetchDocumentType = async (id: number): Promise<DocumentType> => {
  const response = await new smallEodSDK.DocumentTypesApi().documentTypesRead(id);
  return response;
};
