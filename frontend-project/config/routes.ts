const casesRoutes = {
  name: 'cases',
  icon: 'FileTextOutlined',
  path: '/cases',
  routes: [
    {
      name: 'list',
      icon: 'FileTextOutlined',
      path: '/cases',
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
      path: '/users',
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
  ],
};

export default [
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
                component: './channels/new',
              },
              {
                name: 'list',
                icon: 'FileTextOutlined',
                path: '/channels/list',
                component: './channels/list',
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
];
