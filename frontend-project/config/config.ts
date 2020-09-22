import slash from 'slash2';
import defaultSettings from './defaultSettings';
import themePluginConfig from './themePluginConfig';
const { pwa } = defaultSettings; // preview.pro.ant.design only do not use in your production ;

const { ANT_DESIGN_PRO_ONLY_DO_NOT_USE_IN_YOUR_PRODUCTION } = process.env;
const isAntDesignProPreview = ANT_DESIGN_PRO_ONLY_DO_NOT_USE_IN_YOUR_PRODUCTION === 'site';
const plugins = [
  ['umi-plugin-antd-icon-config', {}],
  [
    'umi-plugin-react',
    {
      antd: true,
      dva: {
        hmr: true,
      },
      locale: {
        enable: true,
        default: 'pl-PL',
        // default true, when it is true, will use `navigator.language` overwrite default
        baseNavigator: true,
      },
      dynamicImport: {
        loadingComponent: './components/PageLoading/index',
        webpackChunkName: true,
        level: 3,
      },
      pwa: pwa
        ? {
            workboxPluginMode: 'InjectManifest',
            workboxOptions: {
              importWorkboxFrom: 'local',
            },
          }
        : false, // default close dll, because issue https://github.com/ant-design/ant-design-pro/issues/4665
      // dll features https://webpack.js.org/plugins/dll-plugin/
      // dll: {
      //   include: ['dva', 'dva/router', 'dva/saga', 'dva/fetch'],
      //   exclude: ['@babel/runtime', 'netlify-lambda'],
      // },
    },
  ],
  [
    'umi-plugin-pro-block',
    {
      moveMock: false,
      moveService: false,
      modifyRequest: true,
      autoAddMenu: true,
    },
  ],
];

if (isAntDesignProPreview) {
  plugins.push([
    'umi-plugin-ga',
    {
      code: 'UA-72788897-6',
    },
  ]);
  plugins.push(['umi-plugin-antd-theme', themePluginConfig]);
}

export default {
  plugins,
  hash: true,
  targets: {
    ie: 11,
  },
  // umi routes: https://umijs.org/zh/guide/router.html
  routes: [
    {
      path: '/',
      component: '../layouts/BlankLayout',
      routes: [
        {
          path: '/user',
          component: '../layouts/UserLayout',
          routes: [
            {
              path: '/user',
              redirect: '/user/login',
            },
            {
              name: 'login',
              icon: 'smile',
              path: '/user/login',
              component: './user/login',
            },
            {
              component: './exception/404',
            },
          ],
        },
        {
          path: '/',
          component: '../layouts/BasicLayout',
          Routes: ['src/pages/Authorized'],
          authority: ['admin', 'user'],
          routes: [
            {
              name: 'cases',
              icon: 'FileTextOutlined',
              path: '/cases',
              routes: [
                {
                  name: 'new',
                  icon: 'FileAddOutlined',
                  path: '/cases/new',
                  component: './cases/new',
                },
                {
                  name: 'list',
                  icon: 'FileTextOutlined',
                  path: '/cases/list',
                  component: './cases/list',
                },
              ],
            },
            {
              name: 'tags',
              icon: 'FileTextOutlined',
              path: '/tags',
              component: './tags/list',
            },
            {
              name: 'letters',
              icon: 'FileTextOutlined',
              path: '/letters',
              routes: [
                {
                  name: 'list',
                  icon: 'HomeOutlined',
                  path: '/letters/list',
                  component: './letters/list',
                },
                {
                  name: 'channels',
                  icon: 'HomeOutlined',
                  path: '/letters/channels',
                  component: './letters/channels',
                },
              ],
            },
            {
              name: 'institutions',
              icon: 'HomeOutlined',
              path: '/institutions',
              routes: [
                {
                  name: 'new',
                  icon: 'FileAddOutlined',
                  path: '/institutions/new',
                  component: './institutions/new',
                },
              ],
            },
            {
              name: 'users',
              icon: 'FileTextOutlined',
              path: '/users',
              component: './users/list',
            },
            {
              path: '/',
              redirect: '/cases/new',
              authority: ['admin', 'user'],
            },
            {
              component: './exception/404',
            },
          ],
        },
      ],
    },
  ],
  // Theme for antd: https://ant.design/docs/react/customize-theme-cn
  theme: {
    // ...darkTheme,
  },
  define: {
    ANT_DESIGN_PRO_ONLY_DO_NOT_USE_IN_YOUR_PRODUCTION:
      ANT_DESIGN_PRO_ONLY_DO_NOT_USE_IN_YOUR_PRODUCTION || '', // preview.pro.ant.design only do not use in your production ; preview.pro.ant.design 专用环境变量，请不要在你的项目中使用它。
  },
  ignoreMomentLocale: true,
  lessLoaderOptions: {
    javascriptEnabled: true,
  },
  disableRedirectHoist: true,
  cssLoaderOptions: {
    modules: true,
    getLocalIdent: (context, _, localName) => {
      if (
        context.resourcePath.includes('node_modules') ||
        context.resourcePath.includes('ant.design.pro.less') ||
        context.resourcePath.includes('global.less')
      ) {
        return localName;
      }

      const match = context.resourcePath.match(/src(.*)/);

      if (match && match[1]) {
        const antdProPath = match[1].replace('.less', '');
        const arr = slash(antdProPath)
          .split('/')
          .map(a => a.replace(/([A-Z])/g, '-$1'))
          .map(a => a.toLowerCase());
        return `antd-pro${arr.join('-')}-${localName}`.replace(/--/g, '-');
      }

      return localName;
    },
  },
  manifest: {
    basePath: '/',
  },
  chainWebpack: config => {
    config.module.rule('small-eod-client').parser({ amd: false });
    config.plugin('env').use(require.resolve('webpack/lib/DefinePlugin'), [
      {
        build_sha: JSON.stringify(process.env.COMMIT_SHA),
        build_branch: JSON.stringify(process.env.COMMIT_BRANCH),
        build_date: JSON.stringify(new Date().toISOString()),
      },
    ]);
  },
  // proxy: {
  //   '/server/api/': {
  //     target: 'https://preview.pro.ant.design/',
  //     changeOrigin: true,
  //     pathRewrite: { '^/server': '' },
  //   },
  // },
};
