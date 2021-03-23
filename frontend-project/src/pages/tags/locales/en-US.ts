export const tagsLocale = {
  tags: {
    fields: {
      name: 'Name',
    },
    modal: { remove: { title: 'Do you want to delete {name} tag?' } },
    list: {
      pageHeaderContent: 'Tags list',
      table: {
        header: 'Tags list',
      },
    },
    detailView: {
      newPageHeaderContent: 'Create Tag',
      editPageHeaderContent: 'Edit Tag',
      placeholders: {
        name: 'Tag name',
      },
      errors: {
        name: 'Name is required',
      },
    },
    errors: {
      fetchFailed: 'Cannot download tags',
      removeFailed: 'Cannot delete tag.',
      updateFailed: 'Editing the tag failed.',
      createFailed: 'Creation of the tag failed.',
    },
  },
};
