#include <stdio.h>
#include <stdlib.h>

/*
a = int(raw_input(’Dame el primer n´umero: ’))
b = int(raw_input(’Dame el segundo n´umero: ’))

if a >= b:
     maximo = a
else:
     maximo = b

print ’El m´aximo es’, maximo
*/

int main(void){
    //declaración de variables
    int a, b, maximo;
    // toma de datos
    printf("Dame el primer número: ");
    scanf("%d", &a);
    
    printf("Dame el segundo número: ");
    scanf("%d", &b);
    
    if (a >= b)
       maximo = a;
    else
        maximo = b;
    
    printf("El máximo es %d\n", maximo);
    
    system("pause");
    return 0;
}


