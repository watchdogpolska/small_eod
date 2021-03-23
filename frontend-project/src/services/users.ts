import { localeKeys } from '@/locales/pl-PL';
import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { User } from './definitions';

const api = new smallEodSDK.UsersApi();

export const UsersService = ReadWriteService<User>({
  readPage: props => api.usersList(props),
  readOne: id => api.usersRead(id),
  create: data => api.usersCreate(data),
  update: (id, data) => api.usersUpdate(id, data),
  remove: id => api.usersDelete(id),
  translations: localeKeys.users.errors,
});
