import slash from 'slash2';
import defaultSettings from './defaultSettings';
const { pwa } = defaultSettings;

const backend_url = process.env.API_URL || 'http://backend:8000/';

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

const casesRoutes = {
  name: 'cases',
  icon: 'FileTextOutlined',
  path: '/cases',
  routes: [
    {
      name: 'list',
      icon: 'FileTextOutlined',
      path: '/cases/list',
      component: './cases/CasesListView',
    },
    {
      name: 'new',
      icon: 'FileAddOutlined',
      path: '/cases/new',
      component: './cases/CasesDetailView',
    },
    {
      name: 'edit',
      path: '/cases/edit/:id',
      component: './cases/CasesDetailView',
      hideInMenu: true,
    },
    { exact: true, path: '/cases', redirect: '/cases/list' },
  ],
};

const usersRoutes = {
  name: 'users',
  icon: 'FileTextOutlined',
  path: '/users',
  routes: [
    {
      name: 'list',
      icon: 'FileTextOutlined',
      path: '/users/list',
      component: './users/UsersListView',
    },
    {
      name: 'new',
      icon: 'FileAddOutlined',
      path: '/users/new',
      component: './users/UsersDetailView',
    },
    {
      name: 'edit',
      path: '/users/edit/:id',
      component: './users/UsersDetailView',
      hideInMenu: true,
    },
    { exact: true, path: '/users', redirect: '/users/list' },
  ],
};

const documentTypesRoutes = {
  name: 'document-types',
  icon: 'FileTextOutlined',
  path: '/documentTypes',
  routes: [
    {
      name: 'list',
      icon: 'FileTextOutlined',
      path: '/documentTypes',
      component: './documentTypes/DocumentTypesListView',
    },
    {
      name: 'new',
      icon: 'FileAddOutlined',
      path: '/documentTypes/new',
      component: './documentTypes/DocumentTypesDetailView',
    },
    {
      name: 'edit',
      path: '/documentTypes/edit/:id',
      component: './documentTypes/DocumentTypesDetailView',
      hideInMenu: true,
    },
  ],
};

const eventsRoutes = {
  name: 'events',
  icon: 'FileTextOutlined',
  path: '/events',
  routes: [
    {
      name: 'list',
      icon: 'FileTextOutlined',
      path: '/events/list',
      component: './events/EventsListView',
    },
    {
      name: 'new',
      icon: 'FileAddOutlined',
      path: '/events/new',
      component: './events/EventsDetailView',
    },
    {
      name: 'edit',
      path: '/events/edit/:id',
      component: './events/EventsDetailView',
      hideInMenu: true,
    },
    { exact: true, path: '/events', redirect: '/events/list' },
  ],
};

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
            casesRoutes,
            {
              name: 'tags',
              icon: 'FileTextOutlined',
              path: '/tags',
              routes: [
                {
                  name: 'new',
                  icon: 'FileAddOutlined',
                  path: '/tags/new',
                  component: './tags/TagsDetailView',
                },
                {
                  name: 'list',
                  icon: 'HomeOutlined',
                  path: '/tags/list',
                  component: './tags/TagsListView',
                },
                {
                  name: 'edit',
                  path: '/tags/edit/:id',
                  component: './tags/TagsDetailView',
                  hideInMenu: true,
                },
              ],
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
              ],
            },
            {
              name: 'channels',
              icon: 'HomeOutlined',
              path: '/channels',
              routes: [
                {
                  name: 'new',
                  icon: 'FileAddOutlined',
                  path: '/channels/new',
                  component: './channels/ChannelsDetailView',
                },
                {
                  name: 'list',
                  icon: 'FileTextOutlined',
                  path: '/channels/list',
                  component: './channels/ChannelsListView',
                },
                {
                  name: 'edit',
                  path: '/channels/edit/:id',
                  component: './channels/ChannelsDetailView',
                  hideInMenu: true,
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
                {
                  name: 'list',
                  icon: 'FileTextOutlined',
                  path: '/institutions/list',
                  component: './institutions/list',
                },
              ],
            },
            {
              name: 'features',
              icon: 'FileTextOutlined',
              path: '/features',
              routes: [
                {
                  name: 'list',
                  icon: 'FileTextOutlined',
                  path: '/features/list',
                  component: './features/list',
                },
              ],
            },
            usersRoutes,
            documentTypesRoutes,
            {
              path: '/',
              redirect: '/cases/new',
              authority: ['admin', 'user'],
            },
            eventsRoutes,
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
        BUILD_SHA: JSON.stringify(process.env.COMMIT_SHA),
        BUILD_BRANCH: JSON.stringify(process.env.COMMIT_BRANCH),
        BUILD_DATE: JSON.stringify(new Date().toISOString()),
      },
    ]);
  },
  proxy: Object.fromEntries(
    ['api', 'admin', 'static', 'media'].map(x => [
      `/${x}/`,
      {
        target: backend_url,
        changeOrigin: true,
      },
    ]),
  ),
};
