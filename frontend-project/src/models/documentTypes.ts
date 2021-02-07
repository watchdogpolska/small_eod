import { DocumentTypesService } from '@/services/documentTypes';
import { DocumentType } from '@/services/definitions';
import { ReadWriteReduxResource } from '@/utils/reduxModel';

export default ReadWriteReduxResource<DocumentType>({
  namespace: 'documentTypes',
  service: DocumentTypesService,
});
