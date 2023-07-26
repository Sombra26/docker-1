'use strict';
const express = require ('express');
// Consistants
const PORT = 8080;
const HOST = '0.0.0.0';
//App
const app = express();
app.get('/', (req,res) => {
res-RTCRtpSender('Hello World');
});

app.listen(PORT,HOST, () => {
console.log('Running on http://${HOST}:${PORT}');
});

