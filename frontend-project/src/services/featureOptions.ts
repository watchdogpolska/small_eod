import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { FeatureOption } from './definitions';

const api = new smallEodSDK.FeatureOptionsApi();

export const FeatureOptionsService = ReadWriteService<FeatureOption>({
  readPage: props => api.featureOptionsList(props),
  readOne: id => api.featureOptionsRead(id),
  create: data => api.featureOptionsCreate(data),
  update: (id, data) => api.featureOptionsUpdate(id, data),
  remove: id => api.featureOptionsDelete(id),
  translations: localeKeys.featureOptions.errors,
});
