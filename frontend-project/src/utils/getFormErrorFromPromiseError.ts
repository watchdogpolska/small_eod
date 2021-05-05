export function getFormErrorFromPromiseError(error: any) {
  return Object.entries(error?.body).map(([name, errors]: [string, Array<string>]) => ({
    name,
    errors,
  }));
}
