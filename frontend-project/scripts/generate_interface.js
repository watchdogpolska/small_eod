const fs = require('fs');

const main = async () => {
    if (process.argv.length < 3) {
        console.error(`${process.argv.slice(0, 2).join("")} [specification-file]`);
        process.exit(-1);
    }
    const spec = JSON.parse(await fs.promises.readFile(process.argv[2]));
    console.log('// This file is generated, do not manually edit this file');
    console.log('// Update and use \'@/scripts/generate_interface.js\' instead');
    console.log('');
    for (const [name, schema] of Object.entries(spec.definitions)) {
        console.log(`export interface ${name} {`);
        for (const [pname, pvalue] of Object.entries(schema.properties)) {
            if (pvalue.type == 'string') {
                console.log(`  ${pname}: string;`);
            } else if (pvalue.type == 'integer') {
                console.log(`  ${pname}: number;`);
            } else if (pvalue.type == 'boolean') {
                console.log(`  ${pname}: boolean;`);
            } else if (pvalue.type == 'array' && pvalue.items.type == 'integer') {
                console.log(`  ${pname}: number[];`);
            } else if (pvalue.type == 'array' && pvalue.items.type == 'string') {
                console.log(`  ${pname}: string[];`);
            } else if (pvalue.type == 'array' && pvalue.items['$ref']) {
                const name = pvalue.items['$ref'].replace('#/definitions/', '');
                console.log(`  ${pname}: ${name}[];`);
            } else {
                console.log(`  // Unsupported type '${pvalue.type}' in ${name}/${pname}`);
                console.log(`  ${pname}: any;`);
            }
        }
        console.log(`}`);
        console.log(``);
    }
};

main().catch(err => {
    console.log(err);
    process.exit(-1);
})
