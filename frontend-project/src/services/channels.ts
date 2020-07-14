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

export const fetchOne = async (id: number): Promise<Channel> => {
  return new smallEodSDK.ChannelsApi().channelsRead(id);
};
