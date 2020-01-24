const Client = require('ssh2').Client;
const tar = require('tar-fs');
const { Transform } = require('stream')
module.exports = (connInfo, srcDir, destDir) => new Promise((resolve, reject) => {
    const archiveStream = tar.pack(srcDir);
    const conn = new Client();
    conn.on('ready', function () {
        console.log('Client :: ready');
        conn.exec(`tar xvf - -C ${destDir}`, function (err, stream) {
            if (err) return reject(err);
            console.log('Exec :: ready');
            let count = 0;
            stream.on('error', (err) => {
                conn.end();
                return reject(err);
            }).on('close', function (code, signal) {
                console.log('Stream :: close :: code: ' + code + ', signal: ' + signal);
                return resolve(conn.end());
            }).on('data', function (data) {
                console.log('STDOUT: ' + data);
            }).stderr.on('data', function (data) {
                console.log('STDERR: ' + data);
            });
            archiveStream.pipe(new Transform({
                transform(chunk, encoding, callback) {
                    count += chunk.length;
                    console.log('Transferred bytes:', count)
                    return callback(null, chunk);
                }
            })).pipe(stream);
        });
    }).on('error', reject)
        .connect(connInfo);
});

if (require.main === module) {
    module.exports({
        host: process.argv[2],
        username: process.argv[3],
        password: process.argv[4],
        debug: console.log,
    }, './', '/tmp/a/')
        .then(console.log)
        .catch(console.error);
}
