// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAM 10

int main(void)
{
    FILE * fin, *fout;
    char letra;
    char letras[TAM];
    int contador = 0, i, leido;
    
    // 1. Abrir y comprobar apertura
    fin = fopen("letras.txt", "r");
    if (fin == NULL)
       {
            perror("Apertura letras");
            system("pause");
            exit(1);
            }
    // creo fichero escritura texto
    fout = fopen("salida.txt", "a");
    if (fout == NULL)
       {
            perror("Apertura salida");
            system("pause");
            exit(1);
            }
    // 2. Lectura secuencial con fgetc
    letra = fgetc(fin);
    while (! feof(fin) )
    {
          contador++;
          letra = fgetc(fin);
          }
    printf("El fichero tiene %d letras\n", contador);
    // Escribe este mensaje en un archivo
    fprintf(fout, "El fichero tiene %d letras\n", contador);

    // Volver al inicio
    // fseek(fin, 0L, 0);
    rewind(fin);
    fgets(letras, TAM, fin);
    while (! feof(fin) ) 
    {
          for (i=0; i<strlen(letras); i++)
              fprintf(fout, "%c(%d)-", letras[i], letras[i]);
          fprintf(fout, "-- >  He leido: %d\n", strlen(letras));
          
          fgets(letras, TAM, fin);
          }
    // Lectura con fread --> bloques de bytes
    rewind(fin);
    leido = fread(letras, sizeof(char), TAM-1, fin);
    while (leido)
    {
          letras[leido]= '\0';  // fread no coloca el NULL
          for (i=0; i<strlen(letras); i++)
              printf("%c(%d)-", letras[i], letras[i]);
          printf("-- >  He leido: %d\n", leido);
          // copio en el fichero lo leido
          fwrite(letras, leido, 1, fout);
          
          // vuelvo a leer
          leido = fread(letras, sizeof(char), TAM-1, fin); 
          
          }
    
    fputs("hola o algo más largo", fout);
    for (i=0; i< 10; i++)
        fprintf(fout, "Linea numero: %d\n", i+1);
    // x. Cerrar fichero
    fclose(fin);
          
    
    

  system("pause"); // Detiene la consola
  
}







