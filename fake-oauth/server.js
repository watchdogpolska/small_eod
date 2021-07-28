/**
 * A *very* simple server, redirecting all requests to a specified url.
 */
const https = require("https");
const fs = require("fs");
const url = require("url");

const PORT = 5678;

// Read generated self-signed certificate to serve https.
// See the Dockerfile for details.
const options = {
  key: fs.readFileSync("key.pem"),
  cert: fs.readFileSync("cert.pem"),
};

console.log(`Starting a server at :${PORT}`);

https
  .createServer(options, function (req, res) {
    const q = url.parse(req.url, true).query;
    const { redirect_uri } = q;

    if (!redirect_uri) {
      throw new Error("redirect_uri must be specified");
    }

    // The content doesn't matter - it's hardcoded in the server.
    // The only important bit is the Location header - the backend should
    // provide a url it would normally expect the oauth server to redirect to.
    // NOTE: the url must be absolute, not docker friendly, i.e. it should
    // start with "localhost", not "backend-project".
    res.writeHead(302, { Location: redirect_uri });
    res.end("Fake oauth reply");
  })
  .listen(PORT);
