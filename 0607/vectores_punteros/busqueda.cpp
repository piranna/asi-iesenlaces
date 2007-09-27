// $Id$

// Algoritmos de búsqueda en vectores.

#include <stdio.h>
#include <stdlib.h>

int bus_secuencial(int v[], int x, int N)
// devuelve la posición del elemento x dentro del vector v
// si no existe, devuelve 0
{
      int i=0;
      for(i=0; i<N; i++)
          if (x==v[i])
             return i;
      return -1;
}

int bus_secuencial_ord(int v[], int x, int N)
// devuelve la posición del elemento x dentro del vector v
// si no existe, devuelve 0
{
      int i=0;
      for(i=0; i<N && x < v[i]; i++)
          if (x==v[i])
             return i;
      return -1;
}     

int bus_binaria(int v[], int x, int N)
// búsqueda en un vector ordenado
{
    int izq = 0, cen, der=N-1, sw=0;
    while(izq<=der & sw==0)
    {
        cen = (izq+der)/2;
        if (v[cen] == x )
           sw = 1;
        else if (x>v[cen])
             izq=cen+1;
        else
            der = cen-1;
    }
    if (sw ==1)
       return cen;
    else
        return -1;
}

void imprime(int v[], int pos)
{
     if (pos == -1)
        printf("El elemento no existe\n");
     else
         printf("%d\n", v[pos]);
     }

int main(void)
{
    int vector[10]={1,2,3,4,5,6,7,8,9,10}, pos;
    // busco 4 en mi vector:
    
    pos = bus_secuencial(vector, 4, 10);
    imprime(vector, pos);
    // busco 14 en mi vector:
    pos = bus_secuencial(vector, 14, 10);
    imprime(vector, pos);
    system("pause"); // Detiene la consola
  
}
