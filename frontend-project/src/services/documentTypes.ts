import smallEodSDK from '@/utils/sdk';

export interface DocumentType {
  id: number;
  name: string;
}

export const fetchOne = async (id: number): Promise<DocumentType> => {
  return new smallEodSDK.DocumentTypesApi().documentTypesRead(id);
};
