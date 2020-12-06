import { FeaturesService } from '@/services/features';
import { Feature } from '@/services/definitions';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<Feature>({
  namespace: 'features',
  service: FeaturesService,
});
