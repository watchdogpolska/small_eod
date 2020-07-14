import smallEodSDK from '@/utils/sdk';

import { PaginationParams, PaginationResponse } from '@/services/common.d';

export interface Channel {
  id: number;
  name: string;
  city: boolean;
  voivodeship: boolean;
  flatNo: boolean;
  street: boolean;
  postalCode: boolean;
  houseNo: boolean;
  email: boolean;
  epuap: boolean;
}

export const fetchOne = async (id: number): Promise<Channel> => {
  return new smallEodSDK.ChannelsApi().channelsRead(id);
};

export async function fetchPage({
  current,
  pageSize,
}: PaginationParams): Promise<PaginationResponse<Channel>> {
  const sdkResponse = await new smallEodSDK.ChannelsApi().channelsList({
    limit: pageSize,
    offset: pageSize * (current - 1),
  });

  return {
    data: sdkResponse.results,
    total: sdkResponse.count,
  };
}
