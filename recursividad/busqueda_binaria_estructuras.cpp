// $Id$
// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>

struct dato{
       int matricula;
       char nombre[20];
       int nota;
       };


int bus_bin_rec(struct dato v[], int x, int izq, int der)
/* buscamos en el vector v el valor x. 
El programa busca el valor de x en el campo matrícula.
*/
{
    int cen;   
           
    cen = (izq+der)/2;
    if(v[cen].matricula == x)  // depende del tipo de datos del vector
            return cen;
    else if (izq > der)
            return -1;
    else if(x>v[cen].matricula)  // depende del tipo y de lo buscado
            return bus_bin_rec(v, x, cen+1, der);
    else
            return bus_bin_rec(v, x, izq, cen-1);

}
              

int main(void)
{
    struct dato alumnos[256], temp;
    int  i, resultado;
    // inicializar vector de prueba
    for (i=0; i< 256; i++)
    {   
        temp.matricula = i;
        alumnos[i]=temp;
        }
        
    // resultado = bus_bin(pares, 101, 256);
    resultado = bus_bin_rec(alumnos, 80, 0, 255);
    if (resultado == -1)
       printf("El elemento no está en el vector\n");
    else
        printf("El alumno buscado está en la posición %d (--> %d)\n", 
                   resultado, alumnos[resultado].matricula );
        
  system("pause"); // Detiene la consola
  
}






