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
  const response = await new smallEodSDK.InstitutionsApi().institutionsRead(id);
  return response;
};

function fetchAllPages(page) {
  if (page.next) {
    const params = new URL(page.next).searchParams;
    return smallEodSDK
      .tagsList({
        limit: params.get('limit'),
        offset: params.get('offset'),
      })
      .then(newPage => {
        const nextPage = newPage;
        nextPage.results = page.results.concat(nextPage.results);
        return fetchAllPages(nextPage);
      });
  }

  return page;
}

export async function fetchAll() {
  smallEodSDK.InstitutionsApi();

  return smallEodSDK.institutionsList().then(page => fetchAllPages(page));
}
