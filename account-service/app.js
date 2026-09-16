const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Account Service Running');
});

server.listen(3000, () => {
  console.log('Account Service running on port 3000');
});
