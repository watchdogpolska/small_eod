export function getFormErrorFromPromiseError(error: any) {
  return Array.from(
    Object.entries(error?.errorBody),
  ).map(([name, errors]: [string, Array<string>]) => ({ name, errors }));
}
