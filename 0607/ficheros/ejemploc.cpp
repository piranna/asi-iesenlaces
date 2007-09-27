// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(void)
{
    FILE * f;  // estructura para manejar un fichero
    char cadena[48];
    char mensaje[81];
    int n=1;
    char letra;
    extern int errno;
    
    // abrir un fichero  --> fopen(nombre, modo)
    f = fopen("ejemplssoc.cpp", "r");
    if (! f)
    {
          perror("fopen");
          printf("%s", mensaje);
          system("pause"); // Detiene la consola
          exit(1);
          }
    // leer de fichero
    // fgetc(f) getc(f) -- > devuelven el carácter leído
    // fgets(cadena, tam, f)  --> devuelve cadena: lee tam-1 como max
    //                        --> devuelve null si fin de fichero o error
    
    while ( fgets(cadena, 48, f) != NULL)
    {
          printf("[%3d]  %s\n", n, cadena);
          n +=1;
          }     
   
    fseek(f, 0L, 0);  // volver al inicio  :  como el seek de python
                      // 0: desde el inicio
                      // fseek(f, 0L, 2) --> al final
                      // fseek(f, -1L, 1) --> en la posición anterior a la leída
    //// leer con getc o fgetc
    letra = getc(f);
    while ( !feof(f) )  /// feof() detecta si hemos alcanzado el fin de fichero
    {
         printf("%c-", letra);
         letra = getc(f);
         }
    
    
    fclose(f);
    
    system("pause"); // Detiene la consola
}







