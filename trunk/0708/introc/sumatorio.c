#include <stdio.h>
#include <math.h>

// siempre función principal: main 
/* devuelve entero, void: indeterminado */
int main(void)
{
   /* obligatorio marcar inicio y final de bloque con {} */
   
   int a, b, i;  /* obligatorio declarar variables: 
                    tipo y nombre*/ 
                    /* sentencias acaban con ;  */
   float s;
   
   /* límites */
   printf("Límite inferior: ");
   scanf("%d", &a);  /* lee de la pantalla.
                     Indicar: tipo de dato y dirección de var */
   while (a < 0){
         printf("No puede ser negativo\n");
         printf("Límite inferior: ");
         scanf("%d", &a);
   }
   
   printf("Límite superior: ");
   scanf("%d", &b); 
   
   while (b < a){
         printf("No puede ser menor que %d", a);
         printf("Límite superior: ");
         scanf("%d", &b);
   }
   
   /* cálculo del sumatorio */
   s = 0.0;
   for (i = a; i<=b; i++){
       s += sqrt(i);
       }
   printf("Sumatorio de raíces ");
   printf("de %d a %d: %.2f \n", a, b, s);
   
   system("pause");
   return 0;
}
