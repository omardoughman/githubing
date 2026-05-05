const http = require("http");
const https = require("http");

http.createServer(async (req, res) => {

  if (req.url === "/call-python") {

    fetch("http://python:5000/api/data")
      .then(r => r.json())
      .then(data => {
        res.end("Node received: " + JSON.stringify(data));
      })
      .catch(err => {
        res.end("Error: " + err.message);
      });

  } else {
    res.end("Node running");
  }

}).listen(3000);
