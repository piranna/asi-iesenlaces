// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>

int digit(int  pos, int num)
/* función, Digit(N,num) que devuelva el dígito Nésimo
de un número num de tipo entero, teniendo en cuenta que el dígito 0 es el dígito más a la derecha (el menos significativo).
La función devolverá -1 si el número no tiene suficientes dígitos.
12345
*/
{
   int i;
   for(i=0; i<pos  ; i++)
        num = num / 10;
   if ( (num <= 9) && (num > 0) )
        return num;
   else
       { num %= 10;
         if (num == 0)
            return -1;
         else
             return num;
             }
}
  
   
int digit_v2(int  pos, int num)
/* función, Digit(N,num) que devuelva el dígito Nésimo
de un número num de tipo entero, teniendo en cuenta que el dígito 0 es el dígito más a la derecha (el menos significativo).
La función devolverá -1 si el número no tiene suficientes dígitos.
12345
*/
{
   int i;
   for(i=0; i<pos  ; i++)
   {    num = num / 10;
        if (num == 0) return -1;
   }
   if ( (num <= 9) && (num > 0) )
        return num;
   else
       return num %= 10;
}
   
int main(void)
{
    int num=12345678, pos=5;
    printf("Posicion %d de %d es %d\n", pos, num, digit(pos, num) );
    printf("Posicion %d de %d es %d\n", pos, num, digit_v2(pos, num) );
    system("pause"); // Detiene la consola
  
}
