'use strict';
const {PUBSUB_TOPIC} = process.env;
const {getDelegatedGmail, findLabel} = require('./client');
const {labelRequired} = require('./config');

const getUsersEmail = async () => {
  // TODO: Fetch user from small_eod
  // TODO: Verify if it (still) exists in GMail
  return [
    'adam.dobrawy@siecobywatelska.pl',
  ];
};

const setupWatch = async () => {
  const users = await getUsersEmail();
  for (const user of users) {
    const gmail = await getDelegatedGmail(user);
    const label = await findLabel(gmail, labelRequired);
    if (!label) {
      console.log(`Not found label '${labelRequired}' for ${user}. Skipping.`);
      // We do not create a label, as we only
      // have read-only permission to reduce risk.
      continue;
    }
    console.log(`Found label '${label.id}' for ${user}`);
    await gmail.users.watch({
      userId: 'me',
      requestBody: {
        labelIds: [label.id],
        topicName: PUBSUB_TOPIC,
      },
    });
  }
};
// TODO: Periodically call setupWatch function.
// See "Renewing mailbox watch" in https://developers.google.com/gmail/api/guides/push
setupWatch().catch(console.error);
