#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define DEBUG 1

// Estructura de datos para funciones 4 y 5
struct tdatos{
        char ip[16];
        int tam;
    };

int numeroConexiones(FILE *f){
    /* Devuelve el número de conexiones del fichero de logs.
    Cada línea es una nueva conexión, por lo que simplemente contamos el número de líneas*/

    int cont=0; // conexiones
    char linea[256];

    rewind(f); // pone cabeza lectura al inicio
    fgets(linea, 256, f);
    while (! feof(f)){
        cont ++;
        fgets(linea, 256, f);
    }
    return cont;

}


char * ipConexion(char * linea){
    /*devuelve una cadena con la ip de una línea de conexión*/
    char * ip;  // aquí almacenaré la ip
    int i;

    ip = (char *) malloc(sizeof(char) * 20);
    for (i = 0; i< strlen(linea); i++)
        if (linea[i] != ' ' )  // el espacio en blanco marca el final de la ip
            ip[i] = linea[i];
        else {
            ip[i] = '\0'; // coloco el NULL al final de la cadena
            break;
        }

    return ip;
}

int numeroIps(FILE *f){
    /* devuelve el número de ips diferentes. En los requisitos han dicho que habrá un máximo de 256 accesos en el fichero */
    char ips[256][16];  // para almacenar las ips.
    char linea[1024], * nuevaip;
    int numips = 0;
    int i, esta;

    rewind(f);
    fgets(linea, 1024, f);
    while (! feof(f)){
        esta = 0;
        nuevaip = ipConexion(linea);
        for (i=0; i<numips; i++){
            if (strcmp(nuevaip, ips[i]) == 0){
                esta = 1;
                break;
            }
        }
        if (!esta) {
            strcpy(ips[numips], nuevaip);  // coloco la nueva ip encontrada en la matriz
            numips ++; // incremento contador
        }
        fgets(linea, 1024, f);
    }

    #ifdef DEBUG
    for (i=0; i<numips; i++)
        printf("    --> %s\n", ips[i]);
    #endif
    return numips;
}

int tamCon(char linea[]){
    int i;
    for (i=strlen(linea)-1; i>=0; i--)
        if (linea[i] == ' ')
            return atoi(linea+i+1);
    return 0;
}

void guardaABinario(char fichtexto[], char fichbin[]){

    FILE * ft, * fb;

    char linea[1024];

    struct tdatos datos;

    ft = fopen(fichtexto, "rt");
    fb = fopen(fichbin, "wb");


    fgets(linea, 1024, ft);
    while (! feof(ft)){
        strcpy(datos.ip, ipConexion(linea));
        datos.tam = tamCon(linea);
        fwrite(&datos, sizeof(datos), 1, fb);
        fgets(linea, 1024, ft);
    }
    fclose(ft);
    fclose(fb);

}


void ordena(struct tdatos datos[], int t){
    int i, j;
    struct tdatos temp;
    for (i=1; i<t; i++)
        for (j=0; j< t-i; j++)
            if(datos[j].tam < datos[j+1].tam){
                temp = datos[j];
                datos[j] = datos[j+1];
                datos[j+1] = temp;
                }

}



void consumoPorIp(FILE * f){
    struct tdatos datos[256], temp;

    int total = 0, i, esta=0;

    while (fread(&temp, sizeof(temp), 1, f)){
        esta = 0;
        for (i=0; i< total; i++)
            if (!strcmp(datos[i].ip, temp.ip)){
                esta = 1;
                datos[i].tam += temp.tam;
                break;
            }
        if (! esta){
            datos[i] = temp;
            total ++;
        }
    }
    ordena(datos, total);
    #ifdef DEBUG
    for (i=0; i< total; i++)
        printf("%s - %d\n", datos[i].ip, datos[i].tam);
    #endif
}

int main(){

    FILE * f;
    char linea[1024];
    char * ip;
    f = fopen("access.log", "rt");
    printf("Numero de conexiones: %d\n", numeroConexiones(f));

    // imprimo todas las conexiones
    rewind(f);
    fgets(linea, 1024, f);
    while (! feof(f)){
        //printf ("%s",linea);
        ip = ipConexion(linea);
        printf("IP de la conexion: %s (%d)\n", ip, tamCon(linea));
        free(ip);
        fgets(linea, 1024, f);
    }
    printf("IPs diferentes: %d\n", numeroIps(f));
    guardaABinario("access.log", "access.dat");

    fclose(f);
    f = fopen("access.dat", "rb");
    consumoPorIp(f);


}

