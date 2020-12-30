import smallEodSDK from '@/utils/sdk';
import { Letter } from './definitions';
import { ReadWriteService } from './service';

const sdk = new smallEodSDK.LettersApi();

export const LettersService = ReadWriteService<Letter>({
  readPage: props => sdk.lettersListWithHttpInfo(props),
  readOne: id => sdk.lettersReadWithHttpInfo(id),
  create: data => sdk.lettersCreateWithHttpInfo(data),
  update: (id, data) => sdk.lettersUpdateWithHttpInfo(id, data),
  remove: id => sdk.lettersDeleteWithHttpInfo(id),
});
