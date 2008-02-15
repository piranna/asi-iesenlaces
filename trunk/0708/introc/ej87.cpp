/*----------------------------------------------------------------
|  Autor:                                                         |
|  Fecha:                               Versión: 1.0              |
|-----------------------------------------------------------------|
|  Descripción del Programa:                                      |
|   Rellena un vector con 10 números diferentes    
    Los muestra ordenados de menor a mayor                                                          |
| ----------------------------------------------------------------*/

// Incluir E/S y Librerías Standard
#include <stdio.h>
#include <stdlib.h>
#define TAM 10

// Zona de Declaración de Constantes

// Zona de Declaración de Tipos

// Zona de Cabeceras de Procedimientos y Funciones

// Programa Principal
int main()
{
    // Zona de Declaración de Variables del Programa principal
    int numero[TAM], i, aux, validos=0, esta;
    
    while (validos < TAM){
        printf("Introduzca un número: ");
        scanf("%d", &aux);
        esta = 0;  // variable bandera: indica si el número está en el vector
        for (i=0; i<validos; i++)  // si está, activamos bandera
            if (aux == numero[i]){
               esta = 1;
               printf("Repe\n");
               break; 
               }
        if (esta == 0){   // comprobamos si está --> (i == validos)
           numero[validos] = aux;
           validos += 1;  
           }
        }

    // ordenar el vector
    
              
    for (i=0; i<TAM; i++)
        printf("%d, ", numero[i]);
        
    

    system("Pause");    // Hacer una pausa
    return 0;           // Valor de retorno al S.O.
}

// Implementación de Procedimientos y Funciones
