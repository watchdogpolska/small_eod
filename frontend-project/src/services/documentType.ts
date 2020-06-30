import smallEodSDK from '@/utils/sdk';

export interface DocumentType {
  name: string;
}

export const fetchDocumentType = async (id: number): Promise<DocumentType> => {
  const response = await new smallEodSDK.DocumentTypesApi().documentTypesRead(id);
  return response;
};
