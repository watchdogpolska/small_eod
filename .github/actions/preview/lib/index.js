#!/usr/bin/env node
const core = require('@actions/core');
const github = require('@actions/github');
const HyperOneApi = require('hyperone-client');
const uploadSsh = require('./sshTar');
const crypto = require("crypto");
const path = require('path');

const hyperone_token = core.getInput('HYPERONE_TOKEN');
const github_token = core.getInput('GITHUB_TOKEN');

const website_image = core.getInput('HYPERONE_IMAGE') || "h1cr.io/website/nginx-static:latest";
const website_flavour = core.getInput("HYPERONE_FLAVOUR") || "website";
const srcDir = core.getInput("SOURCE") || '.';
const destDir = core.getInput("DESTINATION") || '/data/public/';

const SEPERATOR_START = '<!--hyperone-preview-start-->';
const SEPERATOR_END = '<!-- hyperone-preview-end-->';
const COMMENT_MATCH = /<!--\s*hyperone-preview-start\s*-->([^]+?)<!--\s*hyperone-preview-end\s*-->/gm;

HyperOneApi.ApiClient.instance.authentications.ServiceAccount.accessToken = hyperone_token;
HyperOneApi.ApiClient.defaultHeaders = {
  Prefer: `respond-async,wait=${60 * 60 * 24}`,
};
HyperOneApi.ApiClient.timeout = 10 * 60 * 1000;

const websiteApi = new HyperOneApi.WebsiteApi();

let octokit;

const sha512 = (value) => {
  const salt = crypto.randomBytes(8);
  const hash = crypto
    .createHash('sha512')
    .update(salt)
    .update(value)
    .digest();
  return `${salt.toString('base64')} ${hash.toString('base64')}`;
};
const ensureWebsiteExist = async (name, image, service) => {
  const results = await websiteApi.websiteList({ name: name });
  if (results && results.length > 1) {
    throw new Error(`Ambiguous name. Clean up website name '${name}'. `);
  }
  if (results && results.length == 1) {
    const websiteId = results[0].id;
    await websiteApi.websiteDelete(websiteId);
    core.info(`Previous website '${websiteId}' successfully deleted.`);
  };
  const password = crypto.randomBytes(25).toString('hex');
  core.setSecret(password);
  const hash = sha512(password);
  core.setSecret(hash);
  const website = await websiteApi.websiteCreate({
    name: name,
    image: image,
    service: service,
    credential: {
      password: [
        {
          name: 'initial-action',
          type: 'sha512',
          value: hash
        }
      ]
    },
    tag: {
      gitSha: github.context.sha
    }
  })
  const websiteId = website.id;
  core.info(`New website '${websiteId}' successfully created.`);
  return { website, password };
};

const ensureWebsiteNotExist = async (name) => {
  const results = await websiteApi.websiteList({ name: name });
  if (results && results.length > 1) {
    throw new Error(`Ambiguous name. Clean up website name '${name}'. `);
  }
  if (results && results.length == 1) {
    const websiteId = results[0].id;
    await websiteApi.websiteDelete(websiteId);
    core.info(`Website '${websiteId}' successfully deleted.`);
  };
  core.info(`No website to remove`);
};

const getWebsiteName = (context) => {
  return [
    context.payload.repository.full_name,
    github.context.ref
  ].join("/");
};


const getCreateNote = (website) => {
  return `${SEPERATOR_START}
  ---
  # HyperOne Preview\n\n
  Preview URL: [${website.fqdn}](http://${website.fqdn})
  ${SEPERATOR_END}`;
};

const getDeleteNote = () => {
  return `${SEPERATOR_START}
  ---
  # HyperOne Preview\n\n
  Preview URL: \`removed\`
  ${SEPERATOR_END}`;
};


const updatePullComment = async (note) => {
  const { number } = github.context.payload.pull_request;
  const { repository } = github.context.payload;
  const ctx = {
    owner: repository.owner.login,
    repo: repository.name,
    pull_number: number
  };

  const { data: pr } = await octokit.pulls.get(ctx);
  let body = pr.body;
  const match = body.match(COMMENT_MATCH);
  if (match) {
    body = body.replace(match[0], note)
  } else {
    body = `${body}\n${note}`;
  };
  await octokit.pulls.update({
    ...ctx,
    body: body
  });
}
async function run() {
  try {
    core.info("Started action for preview");
    if (!hyperone_token) {
      throw new Error("Missing input: HYPERONE_TOKEN")
    };
    if (!github_token) {
      throw new Error("Missing input: GITHUB_TOKEN")
    };
    octokit = new github.GitHub(github_token);

    const action = github.context.payload.action;
    const website_name = getWebsiteName(github.context);

    switch(action) {
      case 'opened':
      case 'synchronize':
      case 'reopened':
        const { website, password } = await ensureWebsiteExist(
          website_name,
          website_image,
          website_flavour
        );
        core.setOutput('domain', website.fqdn);
        await new Promise(resolve => setTimeout(resolve, 3 * 1000));
        await uploadSsh({
          host: website.fqdn,
          // host: '62.181.8.96',
          username: website.id,
          password: password,
        }, path.join(process.env.GITHUB_WORKSPACE, srcDir), destDir);
        core.info("Website content uploaded");
        await updatePullComment(getCreateNote(website));
        core.info("PR body updated");
        break;
      case 'closed':
        await ensureWebsiteNotExist(website_name);
        await updatePullComment(getDeleteNote());
      default:
        throw new Error("Unsupported operation: ")
    } 
  }
  catch (error) {
    console.log(error);
    if (error.response) {
      core.warning(`Received response: ${error.response.body}`);
    }
    core.setFailed(error.message);
  }
}

run()