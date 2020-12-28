import component from './pl-PL/component';
import globalHeader from './pl-PL/globalHeader';
import pwa from './pl-PL/pwa';
import settingDrawer from './pl-PL/settingDrawer';
import settings from './pl-PL/settings';
import { menuLocale } from './pl-PL/menu';
import { structuredLocale } from '../utils/structedLocale';
import { casesLocale } from '../pages/cases/locales/pl-PL';
import { globalsLocale } from './pl-PL/globals';
<<<<<<< HEAD
import { channelsLocale } from '../pages/channels/locales/pl-PL';
import { usersLocale } from '../pages/users/locales/pl-PL';
import { tagsLocale } from '../pages/tags/locales/pl-PL';
import { documentTypesLocale } from '../pages/documentTypes/locales/pl-PL';
=======
import { usersLocale } from '../pages/users/locales/pl-PL';
import { tagsLocale } from '@/pages/tags/locales/pl-PL';
import { eventsLocale } from '@/pages/events/locales/pl-PL';
>>>>>>> 1503a76 (CRUD for Events)

const [labels, keys] = structuredLocale({
  ...menuLocale,
  ...globalsLocale,
  ...casesLocale,
  ...channelsLocale,
  ...tagsLocale,
  ...usersLocale,
<<<<<<< HEAD
  ...documentTypesLocale,
=======
  ...eventsLocale,
>>>>>>> 1503a76 (CRUD for Events)
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
