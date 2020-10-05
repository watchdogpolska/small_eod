'use strict';
const { PubSub } = require('@google-cloud/pubsub');
const pubSubClient = new PubSub();

const { PUBSUB_TOPIC } = process.env;

const DELAY = 5000;

async function publishMessageWithCustomAttributes() {
    for (let i=0; i+=10; i++) {
        const dataBuffer = Buffer.from(`${i}`);
        const customAttributes = {
            origin: 'nodejs-sample',
            username: 'gcp',
        };

        const messageId = await pubSubClient
            .topic(PUBSUB_TOPIC)
            .publish(dataBuffer, customAttributes);
        console.log(`Message ${messageId} published on topic '${PUBSUB_TOPIC}'.`);
        await new Promise(resolve => setTimeout(resolve, DELAY));
    }
}

publishMessageWithCustomAttributes().catch(console.error);