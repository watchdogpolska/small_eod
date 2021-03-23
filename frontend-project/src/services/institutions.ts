import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Institution } from './definitions';

const api = new smallEodSDK.InstitutionsApi();

export const InstitutionsService = ReadWriteService<Institution>({
  readPage: props => api.institutionsList(props),
  readOne: id => api.institutionsRead(id),
  create: data => api.institutionsCreate(data),
  update: (id, data) => api.institutionsUpdate(id, data),
  remove: id => api.institutionsDelete(id),
  translations: localeKeys.institutions.errors,
});
