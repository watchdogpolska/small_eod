'use strict';
const {JWT} = require('google-auth-library');
const {google} = require('googleapis');

const getDelegatedGmail = async (user) => {
  const authClient = new JWT({
    keyFile: process.env.GOOGLE_APPLICATION_CREDENTIALS,
    subject: user,
    scopes: [
      'https://www.googleapis.com/auth/gmail.readonly',
    ],
  });
  await authClient.authorize();
  return google.gmail({
    version: 'v1',
    auth: authClient,
  });
};

const findLabel = async (gmail, label) => {
  const res = await gmail.users.labels.list({userId: 'me'});
  return res.data.labels.find((x) => x.name == label);
};

module.exports = {
  getDelegatedGmail,
  findLabel,
};
