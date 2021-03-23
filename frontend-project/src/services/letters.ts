import { localeKeys } from '@/locales/pl-PL';
import smallEodSDK from '@/utils/sdk';
import { Letter, LetterList } from './definitions';
import { ReadWriteService } from './service';

const api = new smallEodSDK.LettersApi();

export const LettersService = ReadWriteService<LetterList, Letter>({
  readPage: props => api.lettersList(props),
  readOne: id => api.lettersRead(id),
  create: data => api.lettersCreate(data),
  update: (id, data) => api.lettersUpdate(id, data),
  remove: id => api.lettersDelete(id),
  translations: localeKeys.letters.errors,
});
