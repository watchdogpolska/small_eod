import { ReadWriteService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { DocumentType } from './definitions';

export const DocumentTypesService = ReadWriteService<DocumentType>({
  readPage: props => new smallEodSDK.DocumentTypesApi().documentTypesListWithHttpInfo(props),
  readOne: id => new smallEodSDK.DocumentTypesApi().documentTypesReadWithHttpInfo(id),
  create: data => new smallEodSDK.DocumentTypesApi().documentTypesCreateWithHttpInfo(data),
  update: (id, data) =>
    new smallEodSDK.DocumentTypesApi().documentTypesUpdateWithHttpInfo(id, data),
  remove: id => new smallEodSDK.DocumentTypesApi().documentTypesDeleteWithHttpInfo(id),
});
