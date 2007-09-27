// $Id$

// ficheros de enteros

#include <stdio.h>
#include <stdlib.h>

void creaFichero(char *nombre)
{
     int i;
     FILE * f;

     f = fopen(nombre, "w");
     if ( f == NULL)
     {
           perror("fopen");
           exit(1);
           system("pause"); // Detiene la consola
           }
     for (i=1; i<1001; i++)
         fprintf(f, "%d ", i);
     fclose(f);
}

void leeFichero(char *nombre)
{
     int i;
     FILE * f;
     f = fopen(nombre, "r");
     if ( f == NULL)
     {
           perror("fopen");
           exit(1);
           system("pause"); // Detiene la consola
           }
     fscanf(f, "%d", &i);
     while (! feof(f) )
      {
          printf("%d\n", i);
          fscanf(f, "%d", &i);
           }
     }
void escribeBinario(char *origen, char *destino)
// escribe en binario el contenido de origen (texto)
{
     int i;   // para almacenar los enteros que leemos del fichero
     FILE * fin, *fout;
     fin = fopen(origen, "r");
     if ( fin == NULL)
     {
           perror("fopen");
           exit(1);
           system("pause"); // Detiene la consola
           }
     fout = fopen(destino, "wb");
     if ( fout == NULL)
     {
           perror("fopen");
           exit(1);
           system("pause"); // Detiene la consola
           }
     fscanf(fin, "%d", &i);
     while (! feof(fin) )
      {
          fwrite(&i, sizeof(i), 1, fout);
          fscanf(fin, "%d", &i);
           }
     fclose(fin);
     fclose(fout);
}

void leeBinario(char *nombre)
{
     int i;   // para almacenar los enteros que leemos del fichero
     FILE * fin;
     fin = fopen(nombre, "rb");
     if ( fin == NULL)
     {
           perror("fopen");
           exit(1);
           system("pause"); // Detiene la consola
           }

     while (fread(&i, sizeof(int), 1, fin))
           printf("%d  ", i);
     fclose(fin);
}



int main(void)
{
     creaFichero("numeros.txt");
     leeFichero("numeros.txt");
     escribeBinario("numeros.txt", "numeros.dat");
     leeBinario("numeros.dat");
     
     system("pause"); // Detiene la consola
  
}











