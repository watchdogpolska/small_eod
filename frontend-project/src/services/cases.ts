import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { Case } from './definitions';

export const CasesService = ReadWriteService<Case>({
  readPage: props => new smallEodSDK.CasesApi().casesListWithHttpInfo(props),
  readOne: id => new smallEodSDK.CasesApi().casesReadWithHttpInfo(id),
  create: data => new smallEodSDK.CasesApi().casesCreateWithHttpInfo(data),
  update: (id, data) => new smallEodSDK.CasesApi().casesUpdateWithHttpInfo(id, data),
  remove: id => new smallEodSDK.CasesApi().casesDeleteWithHttpInfo(id),
});
