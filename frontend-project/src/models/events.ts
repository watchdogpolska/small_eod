import { EventsService } from '@/services/events';
import { Event } from '@/services/definitions';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<Event>({
  namespace: 'events',
  service: EventsService,
});
