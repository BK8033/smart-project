var express =require('express');
var app = express();
var fs = require('fs');


app.engine('html',require('ejs').renderFile);
app.set('view engine','ejs');

app.get('/map',function(req,res){
//	res.render('map.html')
	res.render('map.html')
});

app.get('/login',function(req,res){
	res.render('login.html')
});

app.get('/get_geo',function(req,res){
	res.render('index_ori.html')
});

app.listen(8033,function(){
	console.log('Server Start..');
});
