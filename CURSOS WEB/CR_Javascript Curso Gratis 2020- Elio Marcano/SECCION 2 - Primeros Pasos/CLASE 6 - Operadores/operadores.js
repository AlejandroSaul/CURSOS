console.log('***OPERADORES ARITMETICOS***')
//operadores aritmeticos +,-,*,/,%,**,++,--
var a = 2 //igualacion
console.log(a)

a = 3
a = a + 3 //suma
console.log(a)

a = 3
a = a**3 //potencia
console.log(a)

a = 3
a = a++ //Agrega uno a su operando
console.log(a)

/*OPERADORES DE ASIGANACIÓN (ABREVIACIÓN DE OPERADORES ARITMETICOS)*/
//operadores abreviados +=,-=,*=,/=,%=,**=
//https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_operators
console.log('***OPERADORES DE ASIGANACIÓN***')

a = 3
a /= 3 //división abrrebiada
console.log(a)

a = 3
a **= 3 //Potencia abreviada 
console.log(a)

a = 9
a %= 4 //Módulo abreviada 
console.log(a)

console.log('***OPERADORES DE COMPARACIÓN***')
//Operadores de comparación
a = 2
a2 = '2'
a3 = "2"
console.log(`a=${a}, a2='${a2}', a3 ="${a3}"`)
console.log('a == a2 '+ (a == a2))
console.log('a === a2 '+(a === a2))
console.log('a2 === a3 '+(a2 === a3))

console.log('a != a2 '+(a != a2))
console.log('a !== a2 '+(a !== a2))

console.log('a>a2 '+(a>a2))
console.log('a>=a2 '+(a>=a2))

console.log('***OPERADORES LOGICOS***')
// && (and), || (or), ! (not)
a = true
b = false
console.log('a = true, b = false')
console.log("a&&b "+(a&&b))
console.log("a||b "+(a||b))
console.log("!a "+(!a))

console.log('***OPERADORES CONDICIONAL TERNARIO***')
a == b ? console.log("Es igual"): console.log("No es igual")