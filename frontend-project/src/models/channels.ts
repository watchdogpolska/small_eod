import { ChannelsService } from '@/services/channels';
import { Channel } from '@/services/definitions';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<Channel>({
  namespace: 'channels',
  service: ChannelsService,
});
