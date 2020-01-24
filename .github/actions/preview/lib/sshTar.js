
const Client = require('ssh2').Client;
const tar = require('tar');
const klaw = require('klaw');
const { relative } = require('path')
module.exports = (connInfo, srcDir, destDir) => new Promise((resolve, reject) => {
    // const archiveStream = tar.pack(srcDir);
    const conn = new Client();
    conn.on('ready', () => {
        console.log('Client :: ready');
        conn.exec(`tar xvf - -C ${destDir}`, async (err, stream) => {
            if (err) return reject(err);
            console.log('Exec :: ready');
            const archiveStream = new tar.Pack({
                cwd: srcDir,
            });
            stream.on('error', (err) => {
                conn.end();
                return reject(err);
            })
                .on('close', () => conn.end())
                .on('close', (code, signal) => {
                    console.log('Stream :: close :: code: ' + code + ', signal: ' + signal);
                    if (code !== 0) {
                        return reject(new Error(`Invalid code: ${code}`));
                    }
                    return resolve();
                }).on('data', (data) => {
                    console.log('STDOUT: ' + data);
                }).stderr.on('data', (data) => {
                    console.log('STDERR: ' + data);
                });
            archiveStream.pipe(stream);
            try {
                for await (const { path, stats } of klaw(srcDir)) {
                    const relativePath = relative(srcDir, path);
                    if (!stats.isDirectory()) {
                        archiveStream.add(relativePath);
                        console.log(`Added file: ${path}`)
                    }
                }
            } catch (err) {
                conn.end();
                return reject(err);
            }
            archiveStream.end();
        });
    }).on('error', reject)
        .connect(connInfo);
});

if (require.main === module) {
    module.exports({
        host: process.argv[2],
        username: process.argv[3],
        password: process.argv[4],
    }, './', '/tmp/a/')
        .then(console.log)
        .catch(console.error);
}
