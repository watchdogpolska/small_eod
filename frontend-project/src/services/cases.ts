import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Case } from './definitions';

const api = new smallEodSDK.CasesApi();

export const CasesService = ReadWriteService<Case>({
  readPage: props => api.casesList(props),
  readOne: id => api.casesRead(id),
  create: data => api.casesCreate(data),
  update: (id, data) => api.casesUpdate(id, data),
  remove: id => api.casesDelete(id),
  translations: localeKeys.cases.errors,
});
