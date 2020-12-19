import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Tag } from './definitions';

export const TagsService = ReadWriteService<Tag>({
  readPage: props => new smallEodSDK.TagsApi().tagsListWithHttpInfo(props),
  readOne: id => new smallEodSDK.TagsApi().tagsReadWithHttpInfo(id),
  create: data => new smallEodSDK.TagsApi().tagsCreateWithHttpInfo(data),
  update: (id, data) => new smallEodSDK.TagsApi().tagsUpdateWithHttpInfo(id, data),
  remove: id => new smallEodSDK.TagsApi().tagsDeleteWithHttpInfo(id),
});
