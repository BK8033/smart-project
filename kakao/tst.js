var fs = require('fs');
p = fs.readFileSync('./config.js','utf-8');
console.log(p);
console.log('----------------------------');
console.log('\n\n');
var old = p.substr(222,11);

var newnum = '01064849188';
nw = p.replace(old,newnum);
console.log(p.substr(95,10));
fs.writeFileSync('./config.js',p.replace(old,newnum),'utf8');
console.log('compeleted..');
