import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { DocumentType } from './definitions';

const api = new smallEodSDK.DocumentTypesApi();

export const DocumentTypesService = ReadWriteService<DocumentType>({
  readPage: props => api.documentTypesList(props),
  readOne: id => api.documentTypesRead(id),
  create: data => api.documentTypesCreate(data),
  update: (id, data) => api.documentTypesUpdate(id, data),
  remove: id => api.documentTypesDelete(id),
  translations: localeKeys.documentTypes.errors,
});
