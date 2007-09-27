// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>

int mcd_malo(int x, int y)
{
    int pasos=0, i, max=1;
    if (x > y ) 
    {
          i = x;
          x = y;
          y = i;
}         // ahora x es el menor
    for (i=1; i<=x; i++)
    {
        if ((y % i == 0) && (x % i == 0) )
           max = i;
        //pasos++;
        }
    //printf("Resuelto en %d pasos\n", pasos);
    return max;
}

int mcd(int x, int y)
{
    int resto, pasos=0; 
    if (x<0) x=x*-1; // convertir en positivos
    if (y<0) y=y*-1;
   
   while (y!=0)
   {
             resto=x%y;
             x=y;
             y=resto;
             //pasos++;
   }
   //printf("Resuelto en %d pasos\n", pasos);
   return x;
}

int rmcd( int x, int y )  //método recursivo
{
    if ( y == 0 )
       return x;
    else
        rmcd(y, x%y ); 
}

int mcm(int x, int y)
{
    return x*y/mcd(x,y);
}

int main(void)
{
    int n1 = 6936, n2 = 1200;
    printf("MCD de %d y %d es %d\n", n1, n2, mcd_malo(n1, n2));
    printf("MCD de %d y %d es %d\n", n1, n2, mcd(n1, n2));    
    printf("MCM de %d y %d es %d\n", n1, n2, mcm(n1, n2));    
    system("pause"); // Detiene la consola
  
}
