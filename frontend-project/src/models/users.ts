import { UsersService } from '@/services/users';
import { User } from '@/services/definitions';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<User>({
  namespace: 'users',
  service: UsersService,
});
