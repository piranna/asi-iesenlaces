// $Id$

// Explicacion del programa

#include <stdio.h>
#include <stdlib.h>

/// definición del tipo

struct persona{
       char nombre[30];
       int edad;
       };
       
typedef struct persona tPersona;

void imprime(struct persona p)
// parámetro de entrada
{
     printf("Nombre: %s\nEdad: %d\n", p.nombre, p.edad);
}

void sumaedad(struct persona p_valor, struct persona *p_ref)
// p_valor se pasa por valor, p_ref se pasa por "referencia"
{
     p_valor.edad += 1;
     p_ref->edad += 1;
     }

struct persona sumaedad_ret(struct persona p_valor)
// p_valor se pasa por valor, p_ref se pasa por "referencia"
{
     p_valor.edad += 1;
     return p_valor;
     }     

int main(void)
{
    struct persona alumna = {"Maria", 19};
    tPersona alumno={"Juan", 19}, otroAlumno;
    
    sumaedad(alumna, &alumno); // incremento la edad de las dos variables
    otroAlumno = sumaedad_ret(alumna);
    
    imprime(alumna);
    imprime(alumno);
    imprime(otroAlumno);
    
  system("pause"); // Detiene la consola
  
}
