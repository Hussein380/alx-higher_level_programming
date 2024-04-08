#!/usr/bin/node

// check if there are command line arguments
// the first two are the node executable and the script path
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
