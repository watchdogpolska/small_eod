import { localeKeys } from '@/locales/pl-PL';
import smallEodSDK from '@/utils/sdk';
import { Letter, File as ResourceFile, SignRequest } from './definitions';
import { handleError, ReadWriteService } from './service';

const api = new smallEodSDK.LettersApi();

export const FileService = (letter: Letter) => ({
  uploadFile: (name: string, file: File | Blob) => {
    return handleError<string>(
      (async () => {
        const signRequest: SignRequest = await api.lettersFilesSignCreate({ name });

        const formData = new FormData();
        Array.from(Object.entries(signRequest.formData)).forEach(([key, value]) =>
          formData.append(key, value),
        );
        formData.append('file', file);

        await fetch(signRequest.url, { method: signRequest.method, body: formData });
        return signRequest.path;
      })(),
      localeKeys.files.errors.createFailed,
    );
  },
  ...ReadWriteService<ResourceFile>({
    readPage: props => api.lettersFilesList(letter.id, props),
    readOne: id => api.lettersFilesRead(id, letter.id),
    create: data => api.lettersFilesCreate(letter.id, data),
    update: (id, data) => api.lettersFilesUpdate(id, letter.id, data),
    remove: id => api.lettersFilesDelete(id, letter.id),
    translations: localeKeys.files.errors,
  }),
});
