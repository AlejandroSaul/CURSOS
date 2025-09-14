/* ===========================Ejercicio Interpolacion de cadenas ===========================
 Escribe dentro de interpocacionCadenas una función que devuelva: 
"Mi nombre es Alejandro y tengo 30 años" Usando Interpolacion de cadenas*/

function interpocacionCadenas(){
  nombre = 'Alejandro'
  edad = '30'
  cadena ;
  return cadena
}



/* ===========================
   Ejecucion de pruebas
   =========================== */
test("interpocacionCadenas", interpocacionCadenas, "Mi nombre es Alejandro y tengo 30 años");  


/* ===========================
   Evaluador de ejercicios
   =========================== */
function test(nombreFuncion, funcion, esperado) {
  try {
    let resultado = funcion();
    if (resultado === esperado) {
      console.log(`✅ ${nombreFuncion} pasó la prueba`);
    } else {
      console.log(`❌ ${nombreFuncion} falló. 
        Esperado: "${esperado}" 
        Obtenido: "${resultado}"`);
    }
  } catch (error) {
    console.log(`💥 Error al ejecutar ${nombreFuncion}: ${error.message}`);
  }
}