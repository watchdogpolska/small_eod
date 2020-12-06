import component from './en-US/component';
import globalHeader from './en-US/globalHeader';
import { menuLocale } from './en-US/menu';
import pwa from './en-US/pwa';
import settingDrawer from './en-US/settingDrawer';
import settings from './en-US/settings';
import BaseLocales from './pl-PL';
import { structuredLocale } from '../utils/structedLocale';
import { casesLocale } from '../pages/cases/locales/en-US';
import { globalsLocale } from './en-US/globals';

const [labels] = structuredLocale({
  ...menuLocale,
  ...globalsLocale,
  ...casesLocale,
});

const Locale = {
  'navBar.lang': 'Languages',
  'layout.user.link.help': 'Help',
  'layout.user.link.privacy': 'Privacy',
  'layout.user.link.terms': 'Terms',
  ...globalHeader,
  ...settingDrawer,
  ...settings,
  ...pwa,
  ...component,
  ...labels,
};

// Checking if all keys are in both locale
if (new Set(Object.keys(BaseLocales)) !== new Set(Object.keys(Locale))) {
  const baseLocaleSet = new Set(Object.keys(BaseLocales));
  const localeSet = new Set(Object.keys(Locale));
  const missingLocaleKeys = Array.from(baseLocaleSet).filter(blKey => !localeSet.has(blKey));
  const missingBaseLocaleKeys = Array.from(localeSet).filter(lKey => !baseLocaleSet.has(lKey));

  if (missingLocaleKeys.length > 0)
    console.error(`Missing locale keys: ${missingLocaleKeys.join(', ')}`);
  if (missingBaseLocaleKeys.length > 0)
    console.error(`Missing base locale keys: ${missingBaseLocaleKeys.join(', ')}`);
}

export default Locale;
