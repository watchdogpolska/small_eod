import { defineConfig } from 'umi';
import routes from './routes';

const backend_url = process.env.API_URL || 'http://backend:8000/';

export default defineConfig({
  hash: true,
  antd: {},
  dva: {
    hmr: true,
  },
  history: {
    type: 'browser',
  },
  locale: {
    antd: true,
    default: 'pl-PL',
    // default true, when it is true, will use `navigator.language` overwrite default
    baseNavigator: true,
  },
  dynamicImport: {
    loading: '@/components/PageLoading/index',
  },
  targets: {
    ie: 11,
  },
  pwa: false,
  // umi routes: https://umijs.org/zh/guide/router.html
  routes,
  title: false,
  ignoreMomentLocale: true,
  proxy: Object.fromEntries(
    ['api', 'admin', 'static', 'media'].map(x => [
      `/${x}/`,
      {
        target: backend_url,
        changeOrigin: true,
      },
    ]),
  ),
  manifest: {
    basePath: '/',
  },
  // esbuild: {},
  chainWebpack: config => {
    config.module.rule('small-eod-client').parser({ amd: false });
    config.plugin('env').use(require.resolve('webpack/lib/DefinePlugin'), [
      {
        BUILD_SHA: JSON.stringify(process.env.COMMIT_SHA),
        BUILD_BRANCH: JSON.stringify(process.env.COMMIT_BRANCH),
        BUILD_DATE: JSON.stringify(new Date().toISOString()),
      },
    ]);
  },
});
