#include <stdio.h>

/*
Escribe un programa que pida un número y muestre por pantalla un mensaje:
el número 'x' es capicúa  si es capicúa o el número 'x' no es capicúa si no lo es
*/


int main(){

    int numero, reves=0, copia;  // copia: variable auxiliar,

    printf("Introduzca un número: ");
    scanf("%d", &numero);

    copia = numero;

    // le damos la vuelta al número
    while (copia){
            reves = reves * 10 + copia % 10 ;
            copia = copia / 10;
    }
    if (numero == reves)
        printf("El número %d es capicúa\n", numero);
    else
        printf("El número %d no es capicúa\n", numero);
}
