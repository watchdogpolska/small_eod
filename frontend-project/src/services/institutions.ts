import smallEodSDK from '@/utils/sdk';

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
