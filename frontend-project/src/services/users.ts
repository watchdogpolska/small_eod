import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { User } from './definitions';

export const UsersService = ReadWriteService<User>({
  readPage: props => new smallEodSDK.UsersApi().usersListWithHttpInfo(props),
  readOne: id => new smallEodSDK.UsersApi().usersReadWithHttpInfo(id),
  create: data => new smallEodSDK.UsersApi().usersCreateWithHttpInfo(data),
  update: (id, data) => new smallEodSDK.UsersApi().usersUpdateWithHttpInfo(id, data),
  remove: id => new smallEodSDK.UsersApi().usersDeleteWithHttpInfo(id),
});
