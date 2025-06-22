var express = require('express')
var app = express()

app.use('/',(req,res)=>res.send("Hola Ciapfa"))

app.listen(3000,console.log("Escuchano en el puerto 3000"))
//ejecutamos en la terminal node server
//En el navegador ponemos localhost:3000