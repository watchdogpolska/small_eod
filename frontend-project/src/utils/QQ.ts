// FIXME (mkarol): Add IN, ICONTAINS operators in search grammar

export const QQ = {
  and: (query1: string, query2: string) => {
    if (query1 && query2) return `(${query1} AND ${query2})`;
    if (query1) return query1;
    if (query2) return query2;
    return '';
  },
  or: (query1: string, query2: string) => {
    if (query1 && query2) return `(${query1} OR ${query2})`;
    if (query1) return query1;
    if (query2) return query2;
    return '';
  },
  in: (field: string, query: any[]) => query.map(item => QQ.field(field, item)).reduce(QQ.or),
  icontains: (_: string, query: string) => query,
  field: (field: string, value: any) => (!value ? '' : `${field}: ${value}`),
};
