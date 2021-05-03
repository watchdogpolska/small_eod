export function getFormErrorFromPromiseError(error: any) {
  return Array.from(Object.entries(error?.body)).map(([name, errors]: [string, Array<string>]) => ({
    name,
    errors,
  }));
}
