// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(void)
{
    FILE * f; // fichero para lectura
    char nombre[256], texto[256];
    
    // leer nombre fichero
    // gets no se debería de utilizar NUNCA
    printf("Introduzca el nombre del fichero: ");
    
    fgets(nombre, 256, stdin);  // LECTURA segura del teclado
    
    // abrir el fichero
    
    if ( !(f = fopen(nombre, "r") )  )
       {
               perror("fopen");
               system("pause");
               exit(1);
}
               
    
    
    
     
    system("pause"); // Detiene la consola
  
}
