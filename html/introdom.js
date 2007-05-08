// funciones que usan swapDOM para poner o quitar el mensaje

function muestraMensaje(texto){
// el <p> del mensaje es de class:avisos para controlar el color desde el css
	antiguo = getElement('mensaje');
	nuevo = DIV({'id':'mensaje'}, P({'class':'avisos'}, texto));
	swapDOM (antiguo, nuevo);
	}

// párrafo vacío en el DIV para efecto visual
function borraMensaje(){
	antiguo = getElement('mensaje');
	nuevo = DIV({'id':'mensaje'}, P(''));
	swapDOM (antiguo, nuevo);
}

function mensajeTemporal(){
	muestraMensaje('Este mensaje se autodestruirá en 2 segundos');
	callLater(2,borraMensaje);
}

// ideas para el validador
// Amplíalo para que detecte que sólo hay números
function validaDNI(){
	var dni = getElement('dni');
	muestraMensaje(dni.value+ ' tiene '+dni.value.length+' caracteres.');
	return false;
}
	
