/*----------------------------------------------------------------
|  Autor:  $Id$                                                   |
|  Fecha:  $Date$                             Versión: 1.0        |
|-----------------------------------------------------------------|
|  Descripción del Programa:  Ejercicio 41 del libro              |
|      Es Mayúscula / es minúscula                              |
| ----------------------------------------------------------------*/

// Incluir E/S y Librerías Standard
#include <stdio.h>
#include <stdlib.h>

// Zona de Declaración de Constantes

// Zona de Declaración de Tipos

// Zona de Cabeceras de Procedimientos y Funciones

// Programa Principal
int main()
{
    // Zona de Declaración de Variables del Programa principal
    char letra;
    
    // Leer letra
    printf("Escribe una letra: ");
    scanf("%c", &letra);
    
    // mostrar Mayúscula / minúscula
    if ((letra >= 'a') && (letra <= 'z')){  // && --> and  ; || --> or
       printf("Es minúscula\n");  // no obligatorio llaves porque sólo una sentencia
       printf("\n");
       }
    else
        if ((letra >= 'A') && (letra <= 'Z'))
           printf("Es mayúscula\n");  
        else printf("No es una letra\n");  
    
    // if comprimido   (test) ? loquehace sí : loquehace no ;
    ((letra >= 'a') && (letra <= 'z')) ?  
            printf("--> Es minúscula\n") : 
            printf("--> Es mayúscula\n"); 

    system("Pause");    // Hacer una pausa
    return 0;           // Valor de retorno al S.O.
}

// Implementación de Procedimientos y Funciones




