import { InstitutionsService } from '@/services/institutions';
import { Institution } from '@/services/definitions';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<Institution>({
  namespace: 'institutions',
  service: InstitutionsService,
});
