// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
   int numero, *p_num;
   int vector[5]= {1,2,3,4,5};
   char letra, *p_letra;
   
   printf("%d  -  %c  -  %p\n", numero, letra, p_num );
   numero = 5;
   letra = 'A';
   p_num = &numero;
   
   printf("%d  -  %c\n", numero, letra);
   printf("%d  -  %c  -  %p (%p) - %d\n", 
                  numero, letra, p_num, &numero, *p_num );
                  
   p_num = &vector[0];
   
   for (numero=0; numero < 5; numero ++)
       printf("%d  (%p)\n", *(p_num + numero), p_num + numero);

   for (numero=0; numero < 5; numero ++) 
       *(p_num + numero) *= 2;

   for (numero=0; numero < 5; numero ++)
       printf("%d  (%p)\n", *(p_num + numero), p_num + numero);

  system("pause"); // Detiene la consola
  
  
  
  
  
  
  
  
  
  
  
  
  
}
