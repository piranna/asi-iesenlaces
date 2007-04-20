// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>



struct bloque{
       int numero;
       int basura;
       };
FILE * abrir(void)
{
     FILE *f;
     f = fopen("test.dat", "r+b");
     if (f == NULL)
     {
           perror("Error en test.dat");
           system("Pause");
           exit(1);
           }
     }
void guardar(FILE *f)
{
    int n;
    struct bloque x;
    fseek(f, 0L, SEEK_SET);
    for (n=0; n<10; n++)
        {
              x.numero = n;
              fwrite(&x, sizeof(x), 1, f);
              }
             }
void mostrar(FILE *f)
{
     struct bloque dato;
     fseek(f, 0L, 0);
     while(fread(&dato, sizeof(dato), 1, f) )
     // si puede haber registros no válidos, mostrar sólo los válidos
     if (dato.numero >= 0)
          printf("N: %d\n", dato.numero);
}

void eliminar_a(int n, FILE *f)
{    
     struct bloque dato;
     fseek(f, 0L, 0);
     // buscar la posición
     while ( fread(&dato, sizeof(dato), 1, f ) )
           if (dato.numero == n) 
          // retroceder
          {
             fseek(f, -1L*sizeof(dato), 1);
             dato.numero = -1;
             // reescribir
             fwrite(&dato, sizeof(dato), 1, f);
             break;
             }
}

void desplaza(FILE *f)
{
     struct bloque dato;

     // mientras leer
     while(fread(&dato, sizeof(dato), 1, f))
     {
     // retroceder
     fseek(f, -2L*sizeof(dato), 1);
     fwrite(&dato, sizeof(dato),1, f);
     printf("Muevo %d (%ld) \n", dato.numero, ftell(f));
     fseek(f, 1L*sizeof(dato), 1);
     }
     
     fseek(f, -1L*sizeof(dato), 2);
     printf("Voy a truncar a %ld\n", ftell(f));
     ftruncate(fileno(f), ftell(f));
                         
     // truncar
     
     }

void eliminar_b(int n, FILE *f)
{    
     struct bloque dato;
     fseek(f, 0L, 0);
     // buscar la posición
     while ( fread(&dato, sizeof(dato), 1, f ) )
           if (dato.numero == n) 
              {
              printf("Encontrado!!(%ld) \n\n", ftell(f));
              desplaza(f);
              break;
              }
              }




             
int main(void)
{
    FILE * f;
    struct bloque dato;
    f = abrir();
    //guardar(f);
    eliminar_b(0, f);
    mostrar(f);
    system("pause"); // Detiene la consola
  
}











