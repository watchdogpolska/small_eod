import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Channel } from './definitions';

const api = new smallEodSDK.ChannelsApi();

export const ChannelsService = ReadWriteService<Channel>({
  readPage: props => api.channelsList(props),
  readOne: id => api.channelsRead(id),
  create: data => api.channelsCreate(data),
  update: (id, data) => api.channelsUpdate(id, data),
  remove: id => api.channelsDelete(id),
  translations: localeKeys.channels.errors,
});
