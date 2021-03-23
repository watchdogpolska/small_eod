export const QQ = {
  icontains: (field: string, query: string) => ({ [`${field}Icontains`]: query }),
  in: (field: string, query: any[]) => ({ [`${field}In`]: query.map(String).join(',') }),
};
