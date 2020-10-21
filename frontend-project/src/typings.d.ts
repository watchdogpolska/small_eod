declare module 'slash2';
declare module '*.css';
declare module '*.less';
declare module '*.scss';
declare module '*.sass';
declare module '*.svg';
declare module '*.png';
declare module '*.jpg';
declare module '*.jpeg';
declare module '*.gif';
declare module '*.bmp';
declare module '*.tiff';
declare module 'omit.js';

// google analytics interface
interface Window {
  reloadAuthorized: () => void;
}

/* eslint-disable no-use-before-define */
declare const BUILD_DATE: ?string;
declare const BUILD_BRANCH: ?string;
declare const BUILD_SHA: ?string;
/* eslint-enable no-use-before-define */

declare const REACT_APP_ENV: 'test' | 'dev' | 'pre' | false;
