/* ===========================Ejercicio Interpolacion de cadenas ===========================
Javascript Curso Gratis 2020 - Clase 5 
Escribe dentro de interpocacionCadenas una función que devuelva: 
"Mi nombre es Alejandro y tengo 30 años" Usando Interpolacion de cadenas*/

function interpocacionCadenas(){
  nombre = 'Alejandro'
  edad = '30'
  cadena =`Mi nombre es ${nombre} y tengo ${edad} años`;
  return cadena
}

/* ===========================Ejercicio Funciones Basicas Cadenas ===========================
Javascript Curso Gratis 2020 - Clase 5
Escribe dentro de la función cadenas el codigo necesario para combertir el texto = "Texto" en
minusculas = "texto" mayusculas = "TEXTO" longitud = 5*/

function cadenas() {
  texto       =  "Texto";
  minusculas  = texto.toLowerCase()
  mayusculas  = texto.toUpperCase()
  longitud    = texto.length
  return [minusculas,mayusculas,longitud] 
}

/* ===========================
   Ejercicio Funciones Flecha - Operaciones Básicas
   ===========================
   Javascript Curso Gratis 2020 - Clase 8
   Crea una función llamada ejercicioFlecha que:
   1. Defina una función flecha suma que reciba dos números 10 y 5 y retorne su suma.
   2. Defina una función flecha resta que reciba dos números 10 y 5 y retorne su resta.
   3. Ejecute ambas funciones con valores de ejemplo.
   4. Retorne un arreglo con [resultadoSuma, resultadoResta].
*/

function ejercicioFlecha() {
  // funciones flecha dentro de una función normal
  var suma = (a, b) => a + b;
  var resta = (a, b) => a - b;

  // ejemplos de uso
  let resultadoSuma = suma(10, 5);
  let resultadoResta = resta(10, 5);

  // retornar resultados
  return [resultadoSuma, resultadoResta];
}

/* ===========================
   Ejercicio Funciones Flecha - Métodos Number
   ===========================
   Javascript Curso Gratis 2020 - Clase X
   Crea una función llamada ejercicioNumber que:
   1. Defina una función flecha esEntero que reciba un número y retorne true si es entero.
   2. Defina una función flecha convertirEntero que reciba un string y lo convierta a número entero.
   3. Defina una función flecha convertirDecimal que reciba un string decimal y lo convierta a número decimal con un solo decimal.
   4. Ejecute cada función con valores de ejemplo.
   5. Retorne un arreglo con [resultadoEntero, resultadoEnteroCadena, resultadoDecimal].
*/

function ejercicioNumber() {
  // funciones flecha
  var esEntero = (n) => Number.isInteger(n)
  var convertirEntero = (cadena) => Number.parseInt(cadena)
  var convertirDecimal = (cadenaDecimal) => parseFloat(parseFloat(cadenaDecimal).toFixed(1))

  // ejemplos de uso
  let resultadoEntero = esEntero(5);           // true
  let resultadoNoEntero = esEntero(5.15);      // false
  let resultadoEnteroCadena = convertirEntero("5");   // 5
  let resultadoDecimal = convertirDecimal("5.1333"); // "5.1"

  // retornar resultados
  return [resultadoEntero, resultadoNoEntero, resultadoEnteroCadena, resultadoDecimal];
}