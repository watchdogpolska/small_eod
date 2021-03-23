export const institutionsLocale = {
  institutions: {
    fields: {
      name: 'Name',
      comment: 'Comment',
      createdOn: 'Created on',
      modifiedOn: 'Modified on',
      tags: 'Tags',
      externalIdentifier: 'External identifier',
      administrativeDivision: 'Administrative division',
      address: 'Address',
    },
    list: {
      pageHeaderContent: 'Letters list',
      table: {
        header: 'Letters list',
      },
    },
    detailView: {
      newPageHeaderContent: 'Create institution',
      editPageHeaderContent: 'Edit institution',
      placeholders: {
        name: 'Name',
        externalIdentifier: 'External identifier',
        administrativeDivision: 'Administrative division',
        address: 'Address',
      },
      errors: {
        name: 'Name is required',
        externalIdentifier: 'External identifier is required',
        administrativeDivision: 'Administrative division is required',
        address: 'Address is required',
      },
    },
    errors: {
      fetchFailed: 'Cannot download institutions',
      removeFailed: 'Cannot delete institution.',
      updateFailed: 'Editing the institution failed.',
      createFailed: 'Creation of the institution failed.',
    },
  },
};
