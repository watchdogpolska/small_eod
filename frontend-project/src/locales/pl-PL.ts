import { administrativeUnitsLocale } from '@/pages/administrativeUnits/locales/pl-PL';
import { lettersLocale } from '@/pages/letters/locales/pl-PL';
import { featuresLocale } from '@/pages/features/locales/pl-PL';
import { casesLocale } from '../pages/cases/locales/pl-PL';
import { channelsLocale } from '../pages/channels/locales/pl-PL';
import { documentTypesLocale } from '../pages/documentTypes/locales/pl-PL';
import { eventsLocale } from '../pages/events/locales/pl-PL';
import { tagsLocale } from '../pages/tags/locales/pl-PL';
import { usersLocale } from '../pages/users/locales/pl-PL';
import { structuredLocale } from '../utils/structedLocale';
import component from './pl-PL/component';
import globalHeader from './pl-PL/globalHeader';
import { globalsLocale } from './pl-PL/globals';
import { menuLocale } from './pl-PL/menu';
import pwa from './pl-PL/pwa';
import settingDrawer from './pl-PL/settingDrawer';
import settings from './pl-PL/settings';
import { institutionsLocale } from '../pages/institutions/locales/pl-PL';
import { featureOptionsLocale } from '../pages/featureOptions/locales/pl-PL';
import { notesLocale } from '../pages/notes/locales/pl-PL';
import { loginLocale } from '../pages/login/locales/pl-PL';

const [labels, keys] = structuredLocale({
  ...menuLocale,
  ...globalsLocale,
  ...casesLocale,
  ...channelsLocale,
  ...tagsLocale,
  ...usersLocale,
  ...documentTypesLocale,
  ...eventsLocale,
  ...featuresLocale,
  ...administrativeUnitsLocale,
  ...lettersLocale,
  ...institutionsLocale,
  ...featureOptionsLocale,
  ...notesLocale,
  ...loginLocale,
});
export const localeKeys = keys;

export default {
  'navBar.lang': 'Języki',
  'layout.user.link.help': 'Pomoc',
  'layout.user.link.privacy': 'Prywatność',
  'layout.user.link.terms': 'Regulamin',
  ...globalHeader,
  ...settingDrawer,
  ...settings,
  ...pwa,
  ...component,
  ...labels,
};
