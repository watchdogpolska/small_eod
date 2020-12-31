import { Letter } from '@/services/definitions';
import { LettersService } from '@/services/letters';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<Letter>({
  namespace: 'letters',
  service: LettersService,
});
