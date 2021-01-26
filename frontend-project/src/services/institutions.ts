import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Institution } from './definitions';

export const InstitutionsService = ReadWriteService<Institution>({
  readPage: props => new smallEodSDK.InstitutionsApi().institutionsListWithHttpInfo(props),
  readOne: id => new smallEodSDK.InstitutionsApi().institutionsReadWithHttpInfo(id),
  create: data => new smallEodSDK.InstitutionsApi().institutionsCreateWithHttpInfo(data),
  update: (id, data) => new smallEodSDK.InstitutionsApi().institutionsUpdateWithHttpInfo(id, data),
  remove: id => new smallEodSDK.InstitutionsApi().institutionsDeleteWithHttpInfo(id),
});
