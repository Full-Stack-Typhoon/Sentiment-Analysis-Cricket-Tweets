// Usage: node splitData.js file start-end
// Example: node splitData.js data/testData.json 1-10000

var path = require('path');

var filename = process.argv[2];
var range = process.argv[3].split('-');
var json = require('./' + filename);
console.log(JSON.stringify(json.slice(range[0]-1, range[1])));
