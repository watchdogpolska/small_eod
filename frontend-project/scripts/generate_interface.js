const fs = require('fs');
const { string } = require('prop-types');

const main = async () => {
  if (process.argv.length < 3) {
    console.error(`${process.argv.slice(0, 2).join('')} [specification-file]`);
    process.exit(-1);
  }
  const spec = JSON.parse(await fs.promises.readFile(process.argv[2]));
  console.log('// This file is generated, do not manually edit this file');
  console.log("// Update and use '@/scripts/generate_interface.js' instead");
  console.log('');
  for (const [name, schema] of Object.entries(spec.definitions)) {
    console.log(`export interface ${name} {`);
    for (const [pname, pvalue] of Object.entries(schema.properties)) {
      const nullable = pvalue['x-nullable'];
      let type;
      if (pvalue.type == 'string') {
        type = 'string';
      } else if (pvalue.type == 'integer') {
        type = 'number';
      } else if (pvalue.type == 'boolean') {
        type = 'boolean';
      } else if (pvalue.type == 'array' && pvalue.items.type == 'integer') {
        type = 'number[]';
      } else if (pvalue.type == 'array' && pvalue.items.type == 'string') {
        type = 'string[]';
      } else if (pvalue.type == 'array' && pvalue.items['$ref']) {
        const name = pvalue.items['$ref'].replace('#/definitions/', '');
        type = `${name}[]`;
      } else {
        type = `unknown`;
      }

      if (nullable) {
        console.log(`  ${pname}: ${type} | null;`);
      } else {
        console.log(`  ${pname}: ${type};`);
      }
    }
    console.log(`}`);
    console.log(``);
  }
};

main().catch(err => {
  console.log(err);
  process.exit(-1);
});
