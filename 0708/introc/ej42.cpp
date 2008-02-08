/*----------------------------------------------------------------
|  Autor: $Id$                                                    |
|  Fecha: $Date$                        Versión: 1.0              |
|-----------------------------------------------------------------|
|  Descripción del Programa:                                      |
|     Número más cercano al primero                               |
| ----------------------------------------------------------------*/

// Incluir E/S y Librerías Standard
#include <stdio.h>
#include <stdlib.h>
#include <iostream.h>

// Zona de Declaración de Constantes

// Zona de Declaración de Tipos

// Zona de Cabeceras de Procedimientos y Funciones

// Programa Principal
int main()
{
    // Zona de Declaración de Variables del Programa principal
    int num1, num2, num3, num4, num5;  // para almacenar los numeros
    int cercano;                       // más cercano
    // Pedir los 5 números
    cout << "Escribe cinco números (separados por espacios)" << endl;
    cin >> num1 >> num2 >> num3 >> num4 >> num5;
    
    cercano = num2;  // en cercano almacenaremos el número que buscamos
    if (abs(num3 - num1) < abs(cercano - num1))
       cercano = num3;
    if (abs(num4 - num1) < abs(cercano - num1))
       cercano = num4;
    if (abs(num5 - num1) < abs(num1 - cercano))
       cercano = num5;
    // mostramos solución
    cout << "El número más cercano a " << num1 << " es " 
                                   << cercano << endl;
    
    
    // 
    
    system("Pause");    // Hacer una pausa
    return 0;           // Valor de retorno al S.O.
}

// Implementación de Procedimientos y Funciones
