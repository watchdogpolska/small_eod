export const usersLocale = {
  users: {
    fields: {
      username: 'Username',
      password: 'Password',
      email: 'Email',
      firstName: 'First name',
      lastName: 'Last name',
    },
    list: {
      pageHeaderContent: 'Users list',
      table: {
        header: 'Users list',
      },
    },
    detailView: {
      newPageHeaderContent: 'Create user',
      editPageHeaderContent: 'Edit user',
      placeholders: {
        username: 'Username',
        password: 'Safe and long password',
        email: 'contact@sample.com',
        firstName: 'First name',
        lastName: 'Last name',
      },
      errors: {
        username: 'Username is required',
        password: 'Password is required',
        email: 'Email is required',
      },
    },
    errors: {
      fetchFailed: 'Cannot download users',
      removeFailed: 'Cannot delete user.',
      updateFailed: 'Editing the user failed.',
      createFailed: 'Creation of the user failed.',
    },
  },
};
