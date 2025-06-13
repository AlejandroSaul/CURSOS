var numero = 5
var res = Number.isInteger(numero)
console.log(res)

var numero = 5.15
var res = Number.isInteger(numero)
console.log(res)

var numero = "5"
var res = Number.parseInt(numero)
console.log(res)

var numero = "5.1333"
var res = Number.parseFloat(numero).toFixed(1)
console.log(res+" "+typeof(res))