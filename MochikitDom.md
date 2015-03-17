# DOM con MochiKit #

Mochikit tiene herramientas que simplifican mucho el trabajo con DOM

**Documentacion**: http://mochikit.com/doc/html/MochiKit/DOM.html

**Ejemplo**
```
var rows = [
    ["dataA1", "dataA2", "dataA3"],
    ["dataB1", "dataB2", "dataB3"]
];
row_display = function (row) {
    return TR(null, map(partial(TD, null), row));
}
var newTable = TABLE({'class': 'prettytable'},
    THEAD(null,
        row_display(["head1", "head2", "head3"])),
    TFOOT(null,
        row_display(["foot1", "foot2", "foot3"])),
    TBODY(null,
        map(row_display, rows)));
// put that in your document.createElement and smoke it!
swapDOM(oldTable, newTable);
```

**Algunas funciones**
```
getElement(id)

createDOM(nombre[, atributos[, nodo[, ...]]])

appendChildNodes(node[, childNode[, ...]])

removeElement(node)

swapDOM(dest, src)
```
