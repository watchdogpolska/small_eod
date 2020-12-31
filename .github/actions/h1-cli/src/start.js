'use strict';

const https = require('https');
const os = require('os');
const core = require('@actions/core');
const tc = require('@actions/tool-cache');
const packageInfo = require('../package.json');

const headers = {
    'User-Agent': `${packageInfo.name}/${packageInfo.version} (${os.type()} ${os.release()}; ${process.platform}; ${process.arch}) node/${process.versions.node}`,
};

const fetch = (url) => new Promise((resolve, reject) =>
    https.get(url, { headers }, (res) => {
        const { statusCode } = res;
        const contentType = res.headers['content-type'];
        try {
            if (statusCode !== 200) {
                throw new Error(`Request to '${url}' failed. Status Code: ${statusCode}`);
            } else if (!/^application\/json/.test(contentType)) {
                throw new Error(`Invalid content-type. Expected application/json but received ${contentType}`);
            }
        } catch (err) {
            res.resume();
            return reject(err);
        }
        const chunks = [];
        res.on('data', chunk => chunks.push(chunk));
        res.on('end', () => {
            try {
                res.body = JSON.parse(Buffer.concat(chunks).toString('utf-8'))
            } catch (err) {
                return reject(err)
            }
            return resolve(res);
        });
    }).on('error', reject)
);

const fetchAssetUrl = async (version, platform, scope) => {
    const resp = await fetch(`https://api.github.com/repos/hyperonecom/h1-cli/releases/${version}`);
    const asset = resp.body.assets.find(x => x.name.includes(platform) && x.name.startsWith(scope));
    if (!asset) {
        throw new Error(`Unable to determine version ${version} for scope ${scope} and platform ${platform}`);
    }
    return asset.browser_download_url;
}

const downloadExtract = async (asset_url) => {
    const archive_path = await tc.downloadTool(asset_url);
    if (asset_url.endsWith('.zip')) {
        return tc.extractTar(archive_path);
    } else if (asset_url.endsWith('.tar.gz')) {
        return tc.extractTar(archive_path);
    } if (asset_url.endsWith('.7z')) {
        return tc.extract7z(archive_path);
    }
    throw new Error(`Unsupported archive type: ${archive_path}`);
}

const main = async () => {
    const version = core.getInput('version', { required: true });
    const platform = os.platform();
    const scope = core.getInput('scope', { required: true });
    const tool_name = `${scope}-cli`;
    let tool_path = await tc.find(tool_name, version);
    if (!tool_path) {
        const asset_url = await fetchAssetUrl(version, platform, scope);
        tool_path = await downloadExtract(asset_url);
        core.info(`Successfully installed ${tool_name}`);
        await tc.cacheDir(tool_path, tool_name, version);
    };
    core.addPath(tool_path);
};

main().catch(err => {
    console.error(err);
    console.error(err.stack);
    process.exit(err.code || -1);
})
