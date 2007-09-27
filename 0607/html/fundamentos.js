// mis funciones de javascript 

function borrar(){
// ventana de confirmación. Devuelve verdadero o falso según pulse el usuario en aceptar / cancelar
	return confirm("¿Estás seguro?");
	}
	
function aviso(){
	alert("has pulsado")
	}

// valida un campo de texto: obliga a que no esté vacío
function validar(F){
	if ((F.nombre.value.length == 0) || (F.nombre.value == " ") ){
		alert("El nombre está vacío");
		F.nombre.focus();
		return false;
		}
	return true;
	}
	
// muestra las propiedades del objeto documento en un alert
function propiedades(){
	res = "";
	for (prop in document)
		res += prop +'   ';
	alert(res);
	}
	
// cambia el color de fondo del documento usando una propiedad del objeto
function colorFondo(color) {
	document.bgColor=color;
	}

