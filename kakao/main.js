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
	res.render('index.html')
});

app.get('/user',function(req,res){
	console.log(req.query.id);
    res.render('hello.html',
        {
            token: req.query.id,
            title: 'HI'        
        }
    );
});

app.get('/tst',function(req,res){
       res.render('tst.html')
});

app.listen(8033,function(){
	console.log('Server Start..');
});
