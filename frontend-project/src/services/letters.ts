import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';
import { Letter } from '@/services/swagger';

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
