import { localeKeys } from '@/locales/pl-PL';
import { ReadOnlyService } from '@/services/service';
import smallEodSDK from '@/utils/sdk';
import { AdministrativeUnit } from './definitions';

const api = new smallEodSDK.AdministrativeUnitsApi();

export const AdministrativeUnitsService = ReadOnlyService<AdministrativeUnit>({
  readPage: props => api.administrativeUnitsList(props),
  readOne: id => api.administrativeUnitsRead(id),
  translations: localeKeys.administrativeUnits.errors,
});
