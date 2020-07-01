import { PaginationParams, PaginationResponse } from '@/services/common.d';
import smallEodSDK from '@/utils/sdk';

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

export async function fetchChannelsPage({
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

export const fetchChannel = async (id: number): Promise<Channel> => {
  const response = await new smallEodSDK.ChannelsApi().channelsRead(id);
  return response;
};
