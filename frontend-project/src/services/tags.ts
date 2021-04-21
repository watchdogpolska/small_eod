import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Tag } from './definitions';

const api = new smallEodSDK.TagsApi();

export const TagsService = ReadWriteService<Tag>({
  readPage: props => api.tagsList(props),
  readOne: id => api.tagsRead(id),
  create: data => api.tagsCreate(data),
  update: (id, data) => api.tagsUpdate(id, data),
  remove: id => api.tagsDelete(id),
  translations: localeKeys.tags.errors,
});
