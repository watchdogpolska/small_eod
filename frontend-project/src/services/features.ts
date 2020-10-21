import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';
import { Feature } from './definitions';

export async function fetchFeaturesPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<Feature>> {
  smallEodSDK.FeaturesApi();

  const sdkResponse = await smallEodSDK.featuresList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}

export const fetchOne = async (id: number): Promise<Feature> => {
  return new smallEodSDK.FeaturesApi().featuresRead(id);
};
