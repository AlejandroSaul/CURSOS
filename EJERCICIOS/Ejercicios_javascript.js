/* ===========================Ejercicio Interpolacion de cadenas ===========================
Javascript Curso Gratis 2020 - Clase 5 
Escribe dentro de interpocacionCadenas una función que devuelva: 
"Mi nombre es Alejandro y tengo 30 años" Usando Interpolacion de cadenas*/

function interpocacionCadenas() {
  nombre = "Alejandro";
  edad   = "30";
  cadena ;
  return cadena;
}

/* ===========================Ejercicio Funciones Basicas Cadenas ===========================
Javascript Curso Gratis 2020 - Clase 5
Escribe dentro de la función cadenas el codigo necesario para combertir el texto = "Texto" en
minusculas = "texto" mayusculas = "TEXTO" longitud = 5*/

function cadenas() {
  texto       =  "Texto";
  minusculas  = ""
  mayusculas  = ""
  longitud    = ""
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
  //Escribir codigo desde aquí


  
  //Escribir codigo hasta aquí
  let resultadoSuma = suma(10, 5);
  let resultadoResta = resta(10, 5);

  // retornar resultados
  return [resultadoSuma, resultadoResta];
}

/* ===========================
   Ejercicio Funciones Flecha - Funciones Numericas
   ===========================
   Javascript Curso Gratis 2020 - Clase 9
   Crea una función llamada ejercicioNumber que:
   1. Defina una función flecha esEntero que reciba un número y retorne true si es entero.
   2. Defina una función flecha convertirEntero que reciba un string y lo convierta a número entero.
   3. Defina una función flecha convertirDecimal que reciba un string decimal y lo convierta a número decimal con un solo decimal.
   4. Ejecute cada función con valores de ejemplo.
   5. Retorne un arreglo con [resultadoEntero, resultadoEnteroCadena, resultadoDecimal].
*/

function ejercicioNumber() {
  //Escribir codigo desde aquí

  //Escribir codigo hasta aquí

  let resultadoEntero = esEntero(5)
  let resultadoNoEntero = esEntero(5.15)
  let resultadoEnteroCadena = convertirEntero("5.15")
  let resultadoDecimal = convertirDecimal("5.1333")

  return [resultadoEntero, resultadoNoEntero, resultadoEnteroCadena, resultadoDecimal];
}





/* ===========================
   Ejecucion de pruebas
   =========================== */

// test("interpocacionCadenas",interpocacionCadenas,"Mi nombre es Alejandro y tengo 30 años");
// test("cadenas",cadenas,["texto","TEXTO",5]);
// test("ejercicioFlecha",ejercicioFlecha,[15,5]);
// test("ejercicioNumber",ejercicioNumber,[true,false,5,5.1]);


/* ===========================
   Evaluador de ejercicios
   =========================== */
function test(nombreFuncion, funcion, esperado) {
    try {
        let resultado = funcion();

        // **Nueva lógica de comparación**
        // Si 'resultado' y 'esperado' son arreglos, se realiza una comparación profunda.
        if (Array.isArray(resultado) && Array.isArray(esperado)) {
            // Comparar longitud de los arreglos
            if (resultado.length === esperado.length) {
                // Verificar si todos los elementos son iguales
                if (resultado.every((elemento, indice) => elemento === esperado[indice])) {
                    console.log(`✅ ${nombreFuncion} pasó la prueba`);
                } else {
                    console.log(`❌ ${nombreFuncion} falló.`);
                    console.log(`Esperado: ${JSON.stringify(esperado)}`);
                    console.log(`Obtenido: ${JSON.stringify(resultado)}`);
                }
            } else {
                // Si la longitud es diferente, la prueba falla
                console.log(`❌ ${nombreFuncion} falló.`);
                console.log(`Esperado: ${JSON.stringify(esperado)}`);
                console.log(`Obtenido: ${JSON.stringify(resultado)}`);
            }
        } else {
            // Si no son arreglos, se usa la comparación estándar de JavaScript
            if (resultado === esperado) {
                console.log(`✅ ${nombreFuncion} pasó la prueba`);
            } else {
                console.log(`❌ ${nombreFuncion} falló.`);
                console.log(`Esperado: ${JSON.stringify(esperado)}`);
                console.log(`Obtenido: ${JSON.stringify(resultado)}`);
            }
        }
    } catch (error) {
        console.log(`❌ Error al ejecutar ${nombreFuncion}: ${error.message}`);
    }
}
