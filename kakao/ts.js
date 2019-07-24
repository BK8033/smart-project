const http = require('http');

var server = http.createServer((req,res)=>{
	res.end("hello World");
});

server.listen(8033);
