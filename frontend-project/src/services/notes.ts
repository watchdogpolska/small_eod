import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { NoteList, Note } from './definitions';

const api = new smallEodSDK.NotesApi();

export const NotesService = ReadWriteService<NoteList, Note>({
  readPage: props => api.notesList(props),
  readOne: id => api.notesRead(id),
  create: data => api.notesCreate(data),
  update: (id, data) => api.notesUpdate(id, data),
  remove: id => api.notesDelete(id),
  translations: localeKeys.notes.errors,
});
