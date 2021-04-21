import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Event } from './definitions';

const api = new smallEodSDK.EventsApi();

export const EventsService = ReadWriteService<Event>({
  readPage: props => api.eventsList(props),
  readOne: id => api.eventsRead(id),
  create: data => api.eventsCreate(data),
  update: (id, data) => api.eventsUpdate(id, data),
  remove: id => api.eventsDelete(id),
  translations: localeKeys.events.errors,
});
