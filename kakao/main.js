var express =require('express');
var app = express();
var fs = require('fs');
var body = require('body-parser')

const { config, Group } = require('solapi')


app.engine('html',require('ejs').renderFile);
app.set('view engine','ejs');
app.use(body.json());
app.use(body.urlencoded({extended: true}));

conf = fs.readFileSync('./config.js','utf-8');
place = fs.readFileSync('./place.txt','utf-8');

config.init({
    apiKey: 'NCS3CFAYW7TVC6EP',
    apiSecret: '374ICW9HWOUNT0CBB23KTMXF0EFAHSB4'
})

async function send(message, agent = {}){
    try {
        console.log(await Group.sendSimpleMessage(message,agent));
        console.log('Success..')
    } catch (e) {
        console.log(e)
    }
}

app.get('/map',function(req,res){
	res.render('map.html')
});

app.post('/map',function(req,res){
    var text = 'EMERGENCY! \n\rhttps://map.kakao.com/link/map/' + req.body.v1;
    console.log(req.body.v1);
    send({
        text: text,
        type: 'SMS',
        to: conf.substr(222,11),
        from: '01053658033'
    })

    const request = require('request');
    console.log("111111")
    var options = {
        url:'http://52.43.95.248:5365/realEmer',
        method: 'GET',
        qs : {'condition' : 5}
    }
    request(options, function(error,response,body){
        if ( !error && response.statusCode ==200){
            console.log(body)
        }
    })
    console.log("111111")


});

app.get('/login',function(req,res){
	res.render('login.html')
});

app.get('/get_geo',function(req,res){
	res.render('index.html')
});

app.get('/user',function(req,res){
	console.log("추가된 번호는 ",req.query.numer);
    res.render('user.html',
        {
            token: req.query.numer,
            title: 'HI'        
        }
    );
});

app.post('/login',function(req,res){

    newnum = req.body.phonenum;
    oldnum = conf.substr(222,11);
    conf = conf.replace(oldnum,newnum);
    fs.writeFileSync('./config.js',conf,'utf8');
    console.log(newnum, ' inserted');
    
});



app.get('/tst',function(req,res){
       res.render('tst.html')
});

app.listen(8033,function(){
	console.log('Server Start..');
});
