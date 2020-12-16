import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Feature } from './definitions';

export const FeaturesService = ReadWriteService<Feature>({
  readPage: props => new smallEodSDK.FeaturesApi().featuresListWithHttpInfo(props),
  readOne: id => new smallEodSDK.FeaturesApi().featuesReadWithHttpInfo(id),
  create: data => new smallEodSDK.FeaturesApi().featuesCreateWithHttpInfo(data),
  update: (id, data) => new smallEodSDK.FeaturesApi().featuesUpdateWithHttpInfo(id, data),
  remove: id => new smallEodSDK.FeaturesApi().featuesDeleteWithHttpInfo(id),
});
