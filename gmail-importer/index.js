'use strict';
const {PubSub} = require('@google-cloud/pubsub');
const {getDelegatedGmail, findLabel} = require('./client');
const {labelRequired} = require('./config');

const {PUBSUB_SUBSCRIPTION} = process.env;

const pubSubClient = new PubSub();

console.log(`Consume subscription ${PUBSUB_SUBSCRIPTION}`);

const subscription = pubSubClient.subscription(PUBSUB_SUBSCRIPTION);

const getHeader = (full_message, name) => {
  const header = full_message.payload.headers.find((header) => header.name.toLowerCase() == name.toLowerCase());
  if (header) {
    return header.value;
  }
};

const messageHandler = async (message) => {
  console.log(`Received message ${JSON.stringify(message.id, null, 4)}`);
  let data;
  try {
    data = JSON.parse(message.data);
  } catch (err) {
    console.log('Unable to parse message. Skipping.', err);
    return;
  }
  if (!data.emailAddress) {
    console.log('Invalid format of message. Missing \'emailAddress\'. Skipping.');
    return;
  }
  const gmail = await getDelegatedGmail(data.emailAddress);
  const label = await findLabel(gmail, labelRequired);
  const resp = await gmail.users.history.list({
    userId: data.emailAddress,
    startHistoryId: data.historyId,
    labelId: label.id,
  });

  if (!label) {
    console.log(`Missing label for user ${data.emailAddress}. Skipping`);
    // If the user doesn't have a label then they
    // definitely didn't label the message as required.
    message.ack();
    return;
  }
  if (!resp.data.history) {
    console.log(`Missing changes. Skipping notification.`);
    // Gmail is sending notifications to trigger client sync on any
    // changes eg. thread changes, not just those we are interested in.
    // Such blank messages can precede changes which we are interested in.
    message.ack();
    return;
  }
  const messages = [];
  for (const history of resp.data.history) {
    if (history.messagesAdded) {
      messages.push(...history.messagesAdded.map((x) => x.message));
    }
    if (history.labelsAdded) {
      messages.push(...history.labelsAdded.map((x) => x.message));
    }
    // We are currently not interested in changes to
    // remove labels, messages and more
  }
  const uniqueMessageId = [...new Set(messages.map((x) => x.id))];
  for (const messageId of uniqueMessageId) {
    const resp = await gmail.users.messages.get({
      userId: data.emailAddress,
      id: messageId,
    });
    const full_message = resp.data;
    const subject = getHeader(full_message, 'Subject') || '(no subject)';
    const from = getHeader(full_message, 'From') || '(no \'From\' header)';
    const to = getHeader(full_message, 'To') || '(no \'To\' header)';
    const date = new Date(Number(full_message.internalDate));
    console.log({
      subject,
      from,
      to,
      date,
      snippet: full_message.snippet,
      labels: full_message.labelIds,
    });
    // TODO: Check if the message exists in small_eod
    // TODO: Send raw message to minio
    // TODO: Send all attachments to minio
    // TODO: Create new letter in small_eod
    // const rawResp = await gmail.users.messages.get({
    //   userId: data.emailAddress,
    //   id: messageId,
    //   format: 'raw',
    // });
    // const rawMessage = Buffer.from(rawResp.data.raw, 'base64').toString('utf-8');
    // Memory usage comment:
    // GMail restrict message size to 25 MB
}
  message.ack();
};

// Listen for new messages ...
subscription.on('message', messageHandler);
// ... until timeout is hit
// const timeout = 10;
// setTimeout(() => {
//     subscription.removeListener('message', messageHandler);
//     console.log(`${messageCount} message(s) received.`);
// }, timeout * 1000);
