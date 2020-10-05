const { JWT } = require('google-auth-library');
const { google } = require('googleapis');

const { PUBSUB_TOPIC } = process.env;

const labelRequired = 'small_eod';

const getDelegatedGmail = async (user) => {
    const authClient = new JWT({
        keyFile: process.env.GOOGLE_APPLICATION_CREDENTIALS,
        subject: user,
        scopes: [
            'https://www.googleapis.com/auth/gmail.readonly',
        ]
    });
    await authClient.authorize();
    return google.gmail({
        version: 'v1',
        auth: authClient
    });
}

const getUsersEmail = async () => {
    return [
        'adam.dobrawy@siecobywatelska.pl',
    ]
};

const findLabel = async (gmail, label) => {
    const res = await gmail.users.labels.list({userId: 'me'});
    return res.data.labels.find(x => x.name == 'small_eod');
};

const setupWatch = async () => {
    const users = await getUsersEmail();
    for (const user of users) {
        const gmail = await getDelegatedGmail(user);
        const label = await findLabel(gmail, labelRequired);
        if(!label){
            console.log(`Not found label '${labelRequired}' for ${user}. Skipping.`);
            continue;
        }
        console.log(`Found label '${label.id}' for ${user}`);
        const res = await gmail.users.watch({
            userId: 'me',
            requestBody: {
                labelIds: [label.id],
                topicName: PUBSUB_TOPIC,
            },
        });

        console.log(res.data);
    }
};

setupWatch().catch(console.error);
