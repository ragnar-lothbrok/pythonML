//Simple application
const http = require('http');
const url = require('url');

var server = http.createServer((req, res) =>{
    let pathname = url.parse(req.url).pathname;
    console.log(pathname);
    let body = '';
    req.on('data', chunk => {
        body += chunk.toString(); // convert Buffer to string
    });
    req.on('end', () => {
        console.log(body);
        res.end('ok');
    });
});

server.listen(8080, () => {
    console.log('Server started on port 8080');
});
