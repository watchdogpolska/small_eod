export const eventsLocale = {
  events: {
    fields: {
      name: 'Name',
      date: 'Datetime',
      comment: 'Comment',
      case: 'Case',
    },
    list: {
      pageHeaderContent: 'Events list',
      table: {
        header: 'Events list',
      },
    },
    detailView: {
      newPageHeaderContent: 'Create event',
      editPageHeaderContent: 'Edit event',
      placeholders: {
        name: 'Event name',
        comment: 'Comment to an event',
        date: 'Date and time of an event',
        case: 'Case related to an event',
      },
      errors: {
        name: 'Name is required',
        comment: 'Comment is required',
        date: 'Date and time are required',
        case: 'Case is required',
      },
    },
    errors: {
      fetchFailed: 'Cannot download events.',
      removeFailed: 'Cannot delete event.',
      updateFailed: 'Editing the event failed.',
      createFailed: 'Creation of the event failed.',
    },
  },
};
