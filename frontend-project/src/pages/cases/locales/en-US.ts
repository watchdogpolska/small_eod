export const casesLocale = {
  cases: {
    fields: {
      name: 'Name',
      auditedInstitutions: 'Audited institutions',
      comment: 'Comment',
      createdOn: 'Created on',
      modifiedOn: 'Modified on',
      tags: 'Tags',
      letterCount: 'Letter count',
      notifiedUsers: 'Notified users',
      responsibleUsers: 'Responsible users',
      featureOptions: 'Feature options',
    },
    list: {
      pageHeaderContent: 'Cases list',
      table: {
        header: 'Cases list',
      },
    },
    detailView: {
      newPageHeaderContent: 'Create case',
      editPageHeaderContent: 'Edit case',
      placeholders: {
        name: 'Case name',
        auditedInstitutions: 'Case audits those intitiutions',
        comment: 'Comment to case',
        tags: 'Select tags',
        notifiedUsers: 'Users that will be notified about case',
        responsibleUsers: 'Users that will be responsible about case',
        featureOptions: 'Feature options of a case',
      },
      errors: {
        name: 'Name is required',
        comment: 'Comment is required',
        featureOptions: 'At least one feature option is required',
        tags: 'At least one tag is required',
      },
    },
    errors: {
      fetchFailed: 'Cannot download cases',
      removeFailed: 'Cannot delete case.',
      updateFailed: 'Editing the case failed.',
      createFailed: 'Creation of the case failed.',
    },
  },
};
