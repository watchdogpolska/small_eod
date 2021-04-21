import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Feature } from './definitions';

const api = new smallEodSDK.FeaturesApi();

export const FeaturesService = ReadWriteService<Feature>({
  readPage: props => api.featuresList(props),
  readOne: id => api.featuresRead(id),
  create: data => api.featuresCreate(data),
  update: (id, data) => api.featuresUpdate(id, data),
  remove: id => api.featuresDelete(id),
  translations: localeKeys.features.errors,
});
