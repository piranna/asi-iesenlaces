function otroTel(){
    i++;
    inputPos = getElement('telefonos');
    appendChildNodes(inputPos,  LABEL("Teléfono "+i), INPUT({'type': 'text', 'name':"tel"+i}, i), BR());
}

function initPage() {
    i=0;
    otroTel();
}

addLoadEvent(initPage);

