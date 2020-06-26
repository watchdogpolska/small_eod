import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';

interface File {
  downloadUrl: string;
  letter: number;
}

export interface Letter {
  attachment: File[];
  case: number;
  channel: number;
  comment: string;
  createdBy: number;
  createdOn: string;
  date: string;
  description: number;
  direction: string;
  excerpt: string;
  final: boolean;
  id: number;
  reference_number: string;
  institution: number;
  modifiedBy: number;
  modifiedOn: string;
  name: string;
  ordering: number;
}

export async function fetchLettersPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<Letter>> {
  smallEodSDK.LettersApi();

  const sdkResponse = await smallEodSDK.lettersList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}
