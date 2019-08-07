var request = require('request');

var url = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncLcinfoInqire';
var queryParams = '?' + encodeURIComponent('ServiceKey') + '=DMbhCCZSytC0q3lJ7S%2F8oOvGQrunh7pysqKbDMfe7MFgxHS80avJhGYqOSWkF5iIhMf%2BL4RE%2B976NfIvSp30EA%3D%3D'; /* Service Key*/
queryParams += '&' + encodeURIComponent('') + '=' + encodeURIComponent(''); /* */

res = request({
        url: url + queryParams,
            method: 'GET'
}, function (error, response, body) {
        //console.log('Status', response.statusCode);
            //console.log('Headers', JSON.stringify(response.headers));
                console.log('Reponse received', body);
});

//console.log(res);
