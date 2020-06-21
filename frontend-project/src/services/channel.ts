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

export const fetchChannel = async (id: number): Promise<Channel> => {
  const response = await new smallEodSDK.ChannelsApi().channelsRead(id);
  return response;
};
