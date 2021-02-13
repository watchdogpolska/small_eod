import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Event } from './definitions';

export const EventsService = ReadWriteService<Event>({
  readPage: props => new smallEodSDK.EventsApi().eventsListWithHttpInfo(props),
  readOne: id => new smallEodSDK.EventsApi().eventsReadWithHttpInfo(id),
  create: data => new smallEodSDK.EventsApi().eventsCreateWithHttpInfo(data),
  update: (id, data) => new smallEodSDK.EventsApi().eventsUpdateWithHttpInfo(id, data),
  remove: id => new smallEodSDK.EventsApi().eventsDeleteWithHttpInfo(id),
});
