type Labels = { [key: string]: string };

export function structuredLocale<T>(locales: T): [Labels, T] {
  function camelCaseToKebabCase(label: string) {
    return label
      .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
      .replace(/([A-Z])([A-Z])(?=[a-z])/g, '$1-$2')
      .toLowerCase();
  }

  function buildLabel(baseKey: string, key: string) {
    return key === 'self' ? baseKey : `${baseKey}${baseKey && '.'}${camelCaseToKebabCase(key)}`;
  }

  function generateLables<U>(baseKey: string, subLocales: U) {
    return Array.from(Object.entries(subLocales)).reduce<{ [K in keyof U]: string }>(
      (acc, [key, value]) => ({
        ...acc,
        ...(typeof value === 'string'
          ? { [buildLabel(baseKey, key)]: value }
          : generateLables<typeof value>(buildLabel(baseKey, key), value)),
      }),
      {} as any,
    );
  }

  function generateKeys<U>(baseKey: string, subLocales: U): U {
    return Array.from(Object.entries(subLocales))
      .map(([key, value]) => ({
        [key]:
          typeof value === 'string'
            ? buildLabel(baseKey, key)
            : generateKeys<typeof value>(buildLabel(baseKey, key), value),
      }))
      .reduce<U>((acc, prop) => ({ ...acc, ...prop }), {} as any);
  }

  return [generateLables('', locales), generateKeys('', locales)];
}
