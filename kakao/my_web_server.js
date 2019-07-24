var express =require('express');
var app = express();
var fs = require('fs');

app.get('/',function(req,res){

	var html = fs.readFile('pages/map.html',function(err,html){
	html = " " + html
	console.log('File Read');
	res.write(html);
	res.end();
	});
	res.write('Hell');
});

app.listen(8033,function(){
	console.log('Success');
});
