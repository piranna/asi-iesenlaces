#include <stdio.h>

/*
 Escribe un programa que pida una letra por teclado y muestre la letra
que ha introducido el ususario, la anterior y la siguiente.
Por ejemplo, si el usuario introduce la letra 'c',
el programa mostrará el siguiente mensaje: has introducido la letra c,
la letra anterior es la b y la siguiente es la d.
Se utilizará el alfabeto inglés. La letra anterior a la 'a'
consideremos que es la 'z' y la siguiente a la 'z' la 'a'.
Aplicaremos la misma norma con las mayúscula
*/

int main(){
	char letra, anterior, siguiente;
	printf("Introduzca una letra: ");
	scanf("%c", &letra);

	if ((letra == 'a') || (letra == 'A'))
		anterior = letra + 25;
	else  anterior = letra -1;

	if ((letra == 'z') || (letra == 'Z'))
		siguiente = letra - 25;
	else  siguiente = letra + 1;

	printf("La letra anterior a la '%c' es la '%c' y la siguiente es la' %c'\n",
        letra, anterior, siguiente);

	return 0;
}
