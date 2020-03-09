import request from '@/utils/request';

export async function fetchAll() {
  return request('/api/tags/');
}
