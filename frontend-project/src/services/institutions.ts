import smallEodSDK from '@/utils/sdk';

export interface Institution {
  name: string;
  administrativeUnit: string;
  modifiedBy: number;
  createdBy: number;
  modifiedOn: string;
  createdOn: string;
  email: string;
  city: string;
  epuap: string;
  street: string;
  houseNo: string;
  postalCode: string;
  flatNo: string;
  nip: string;
  regon: string;
}

export const fetchInstitution = async (id: number): Promise<Institution> => {
  smallEodSDK.InstitutionsApi();

  const response = await smallEodSDK.institutionsRead(id);
  return response;
};
