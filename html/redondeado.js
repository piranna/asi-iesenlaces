// función que prepara los efectos buscados
// se pueden seleccionar elementos, clases, ids ..
function efectosVisuales (){
        // roundClass se aplica al elemento indicado. Se puede especificar un class
	MochiKit.Visual.roundClass('h1', null);
	MochiKit.Visual.roundClass('h2','redondo', {corners: 'tl tr'});
        // roundElement se aplica al elemento que tenga el id indicado.
	MochiKit.Visual.roundElement('idredondo', {corners: 'bl'});
}

// llama a la función al cargar la página
MochiKit.DOM.addLoadEvent(efectosVisuales);
