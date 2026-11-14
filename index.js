const express = require("express");
const path = require("path");

const app = express();
const port = process.env.PORT || 3000;

const wbsDir = path.join(__dirname, "Webseite");

const ip = "192.168.179.21"


app.use(express.static(wbsDir));

app.get("/", (req, res) => {
    res.sendFile(path.join(wbsDir, "index.html"));
})


app.listen(port, ip, () => { // ip = 192.168.179.21 - locally
    console.log("Server online!")
    console.log("ip: http://" + ip + ":" + port)
})
