# Funciones #

|muestra\_instrucciones() | Muestra en pantalla las instrucciones del juego|
|:------------------------|:-----------------------------------------------|
| pregunta\_si\_no(pregunta) | Hace una pregunta, recibe la respuesta y devuelve **s** o **n** |
| pregunta\_numero(pregunta, bajo, alto) | Pide un número dentro de un rango. Devuelve el número introducido |
| fichas() | Determina quién comienza. Devuelve la ficha del ordenador o del jugador. |
| nuevo\_tablero() | Crea un nuevo tablero vacío. Devuelve el tablero |
| muestra\_tablero(tablero) | Muestra en pantalla el tablero que recibe. |
| movimientos\_legales(tablero) | Devuelve los movimientos legales de un tablero |
| ganador(tablero) | Determina el ganador. Recibe un tablero y devuelve la ficha ganadora, "empate" o Null |
| mueve\_humano(tablero, ficha) | Averigua el movimiento del jugador. Recibe el tablero y la ficha, devuelve el movimiento  |
| mueve\_maquina(tablero, ficha\_comp, ficha\_jugador)  | Calcula el movimiento del ordenador. Devuelve ese movimiento |
| siguiente\_turno(turno) | Cambia el turno. Recibe pieza, devuelve pieza |
| felicita\_ganador(ganador, ordenador, humano | Felicita al ganador. Recibe la pieza ganadora, la del ordenador y la del humano |