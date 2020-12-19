import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Channel } from './definitions';

export const ChannelsService = ReadWriteService<Channel>({
  readPage: props => new smallEodSDK.ChannelsApi().channelsListWithHttpInfo(props),
  readOne: id => new smallEodSDK.ChannelsApi().channelsReadWithHttpInfo(id),
  create: data => new smallEodSDK.ChannelsApi().channelsCreateWithHttpInfo(data),
  update: (id, data) => new smallEodSDK.ChannelsApi().channelsUpdateWithHttpInfo(id, data),
  remove: id => new smallEodSDK.ChannelsApi().channelsDeleteWithHttpInfo(id),
});
