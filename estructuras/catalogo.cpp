// $Id$

/*
Suponiendo las siguientes declaraciones y definiciones:
struct catalogo {
int cod_p ;
char nom_p[20] ;
char tipo_p[30] ;
};
struct inventario {
struct catalogo cat ;
long exist ;
float precio ;
};
struct inventario inven ;
struct inventario *pinv = &inven ;
a)Referenciar los elementos exist y cod_p utilizando la variable inven.
b)Referenciar los elementos precio y nom_p utilizando el puntero pinv.
c)Introducir por teclado un valor en el elemento exist utilizando inven.
d)Introducir por teclado un valor en el elemento tipo_p utilizando el puntero pinv.
e)Visualizar el valor del elemento cod_p utilizando inven.
f)Visualizar el valor del elemento precio utilizando el puntero pinv.
g)Emplear una sentencia de asignación para convertir el primer carácter del
elemento nom_p en mayúscula.
*/
// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// declaraciones de tipos
struct catalogo {
       int cod_p ;
       char nom_p[20] ;
       char tipo_p[30] ;
       };
struct inventario {
       struct catalogo cat ;
       long exist ;
       float precio ;
       };

int main(void)
{
	float t;
	// variables
    struct inventario inven = {1,"Portatil", "Ordenador", 105, 1200};
    //                      inven2 = {exist:10};  // variable inven1
    
    struct inventario *pinv = &inven ;  // variable pinv == puntero a inven
    
    // a)Referenciar los elementos exist y cod_p utilizando la variable inven.
    printf("exist: %ld , cod_p: %d\n", inven.exist, inven.cat.cod_p);

    strcpy(pinv->cat.nom_p, "Ordenadorcico");
    // b)Referenciar los elementos precio y nom_p utilizando el puntero pinv.
    printf("Precio: %.2f, nom_p: %s\n", pinv->precio, pinv->cat.nom_p );
	printf("Precio: %.2f, nom_p: %s\n", (*pinv).precio , (*pinv).cat.nom_p);
    system("pause"); // Detiene la consola
  
}
