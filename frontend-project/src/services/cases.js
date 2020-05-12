import request from '@/utils/request';

export async function queryInstitutions() {
    return request('/api/institutions');
  }