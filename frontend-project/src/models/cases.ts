import { CasesService } from '@/services/cases';
import { Case } from '@/services/definitions';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<Case>({
  namespace: 'cases',
  service: CasesService,
});
