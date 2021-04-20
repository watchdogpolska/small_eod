import { localeKeys } from '@/locales/pl-PL';
import { handleError, ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { RefreshTokenRequest, Request, TokenResponse, User } from './definitions';

const api = new smallEodSDK.UsersApi();

export const UsersService = {
  auth: () => handleError<Request>(api.usersAuth(), localeKeys.users.errors.authFailed),
  exchange: queryParams =>
    handleError<TokenResponse>(api.usersExchange(queryParams), localeKeys.users.errors.authFailed),
  refresh: (data: RefreshTokenRequest) =>
    handleError<TokenResponse>(api.usersRefresh(data), localeKeys.users.errors.authFailed),
  ...ReadWriteService<User>({
    readPage: props => api.usersList(props),
    readOne: id => api.usersRead(id),
    create: data => api.usersCreate(data),
    update: (id, data) => api.usersUpdate(id, data),
    remove: id => api.usersDelete(id),
    translations: localeKeys.users.errors,
  }),
};
