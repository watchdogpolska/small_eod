import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { EventList, Event } from './definitions';

const api = new smallEodSDK.EventsApi();

export const EventsService = ReadWriteService<EventList, Event>({
  readPage: props => api.eventsList(props),
  readOne: id => api.eventsRead(id),
  create: data => api.eventsCreate(data),
  update: (id, data) => api.eventsUpdate(id, data),
  remove: id => api.eventsDelete(id),
  translations: localeKeys.events.errors,
});
