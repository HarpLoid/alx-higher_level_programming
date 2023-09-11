#!/usr/bin/node

const count = parseInt(process.argv[2], 10);

if (process.argv.length < 3) {
  console.log('Missing number of occurences');
}

for (let i = 0; i < count; i++) {
  console.log('C is fun');
}
