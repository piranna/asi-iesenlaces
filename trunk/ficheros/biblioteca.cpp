// $Id$

// Programa para gestionar biblioteca

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define TAM_AUTOR 60
#define TAM_TIT 120
#define TAM_EDIT 60
#define TAM_FECHA 9
#define NOMBRE_FICHERO "biblioteca.dat"

struct libro {
       char autor[TAM_AUTOR];
       char titulo[TAM_TIT];
       char editorial[TAM_EDIT];
       char fecha[TAM_FECHA];
       int numero;
       };

FILE * abrir_fichero(void)
{
     FILE *f;
     f = fopen(NOMBRE_FICHERO, "r+b");
     if (f == NULL)
     {
           perror("Abriendo biblioteca: ");
           system("pause");
           exit(1);
           }

     return f;
}

void inserta_libro(FILE *f)
{
     struct libro miLibro;
     
     printf("Autor: ");
     gets(miLibro.autor);
     printf("Inserto autor --> %s (Tamaño: %d)\n", miLibro.autor, sizeof(miLibro));
     fseek(f, 0L, 2);  // nos colocamos al final !!!!
     fwrite(&miLibro, sizeof(miLibro), 1, f);
     }

void leer_fichero(FILE *f)
{
     struct libro miLibro;
     fseek(f, 0L, 0);
     while ( fread(&miLibro, sizeof(miLibro), 1, f) )
           printf("Autor: %s\n", miLibro.autor);
     
     }
void modificar(int pos, FILE *f)
// modificará el elemento número pos de f
{
     struct libro miLibro;
     // leer y mostrar el contenido
     fseek(f, 1L *(pos-1) * sizeof(miLibro) ,0);
     fread(&miLibro, sizeof(miLibro), 1, f);
     printf("Autor a modificar: %s.\nIntroduzca nuevo autor: ", miLibro.autor);
     // pedir nuevo contenido
     gets(miLibro.autor);
     // escribir el nuevo contenido
     fseek(f, -1L * sizeof(miLibro) ,1);
     fwrite(&miLibro, sizeof(miLibro), 1, f);
     }

void trunca(int pos, FILE * f)
{
     
     ftruncate(fileno(f), sizeof(struct libro)* pos * 1L);
     }

int main(void)
{
    // declaración variables
    struct libro miLibro;
    FILE  *f;
    int i;
    // abrir el fichero: lectura y escritura en binario
     f= abrir_fichero();

    // inserto tres libros
    //for (i=0; i<3; i++)
    //    inserta_libro(f);
        
    // leer todos los datos del fichero
    leer_fichero(f);
    
    modificar(1,f);
    trunca(1, f);
    leer_fichero(f);
    // cerrar fichero
    fclose(f);
    
    system("pause"); // Detiene la consola
}









