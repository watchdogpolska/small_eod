'use strict';
const { PubSub } = require('@google-cloud/pubsub');

const { PUBSUB_SUBSCRIPTION } = process.env;

const pubSubClient = new PubSub();

console.log(`Consume subscription ${PUBSUB_SUBSCRIPTION}`);

// References an existing subscription
const subscription = pubSubClient.subscription(PUBSUB_SUBSCRIPTION);

let messageCount = 0;

const messageHandler = message => {
    console.log(`Received message ${message.id}:`);
    console.log(`\tData: ${message.data}`);
    console.log(`\tAttributes: ${JSON.stringify(message.attributes, null, 4)}`);
    messageCount += 1;
    message.ack();
};

// Listen for new messages ...
subscription.on('message', messageHandler);
// ... until timeout is hit
const timeout = 10;
setTimeout(() => {
    subscription.removeListener('message', messageHandler);
    console.log(`${messageCount} message(s) received.`);
}, timeout * 1000);
