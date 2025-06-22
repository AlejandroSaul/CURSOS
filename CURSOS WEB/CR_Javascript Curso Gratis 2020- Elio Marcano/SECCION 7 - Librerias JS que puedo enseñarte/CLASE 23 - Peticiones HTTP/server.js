var express = require('express')
var app = express()

//app.use('/',(req,res)=>res.send("Hola Ciapfa 3"))
//app.use('/home',(req,res)=>res.send("Hola Ciapfa home"))
app.get('/home',(req,res)=>res.send("Hola Ciapfa home get"))
app.post('/home',(req,res)=>res.send("Hola Ciapfa home post"))

app.listen(3000,console.log("Escuchano en el puerto 3000"))
//ejecutamos en la terminal node server
//En el navegador ponemos localhost:3000

//Cuando nosotros realizamos un cambio una vez que inicializamos el servidor de node, este no se visualiza
//Para que estos cambios se logrn visualizar cada vez que realizamos un cambio debemos instalar una dependencia con npm i nodemon