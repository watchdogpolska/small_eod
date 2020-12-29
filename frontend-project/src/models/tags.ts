import { TagsService } from '@/services/tags';
import { Tag } from '@/services/definitions';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<Tag>({
  namespace: 'tags',
  service: TagsService,
});
