#include <stdio.h>
#define MAX 10

/*
 Escribe un programa que pida al usuario números positivos (un máximo de 50).
 El programa terminará cuando el usuario introduzca 50 números o un número negativo.
 El programa almacenará los números en un vector.
 El programa mostrará en pantalla la siguiente información: cuántos números ha introducido
 el usuario, cuál es el mayor, cuál el menor y la media
 */


 int main(){
     int numeros[MAX], numero=0; //números: vector para almacenar los valores.
     int total=0, i;  //total: números válidos introducidos. i: auxiliar
     int max, min, suma;


     // pido los números
     while (total < MAX && numero >=0) {
         printf("Introduzca un número (negativo para terminar): ");
         scanf("%d", &numero);
         if (numero >= 0){
            numeros[total] = numero;
            total++ ;
         }
     }

     if (total >= 1){
         // inicializo variables
         max = numeros[0];
         min = numeros[0];
         suma = numeros[0];
         for (i=1; i<total; i++){  //el primer elemento ya lo hemos mirado
             numero = numeros[i];
             suma += numero;
             if (numero > max) max = numero;
             if (numero < min) min = numero;
         }
         // resultados
         printf("Números introducidos: %d\n", total);
         printf("Número mayor: %d\n", max);
         printf("Número menor: %d\n", min);
         printf("Media: %.2f\n", (float)suma/total);
     }
     else
         printf("No se han introducido números válidos\n");

 }
