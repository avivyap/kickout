# kickout
La herramienta que he desarrollado combina Scapy, una poderosa librería de Python para la manipulación de paquetes, con Tkinter, una biblioteca para la creación de interfaces gráficas. Esta combinación nos permite crear una herramienta que permita al atacante "expulsar" a la victima de la red.

Digo que la herramienta "expulsa" a la victima por que no es del todo asi, lo que hace es que la victima deje de recibir paquetes de conexion, pero las paginas web en las que tenga en la cache si le funcionaran 

La herramienta es de boton gordo por lo que es super sencilla de usar, simplemente ejecutas el script y ya esta se te abre la siguiente interfaz

<img width="399" height="329" alt="image" src="https://github.com/user-attachments/assets/ac9e835d-2167-4a49-9ddc-3ab0b1079b33" />

Funcionamiento:

Interfaz Gráfica Intuitiva: La aplicación cuenta con una interfaz amigable donde los usuarios pueden interactuar fácilmente con las funciones avanzadas de Scapy. A través de botones y cuadros de texto, se pueden ingresar parámetros y ejecutar acciones sin necesidad de tener conocimientos avanzados de programación ni de ciberseguridad.

Envío de Paquetes ARP: Utilizando Scapy, la herramienta permite enviar paquetes ARP (Address Resolution Protocol) a dispositivos en la red. Lo que permite que nos pongamos en medio del router y la maquina victima (lo que se conoce como un ataque MitM), la unica diferencia es que en un ataque MitM reenviamos los paquetes que nos llegan del router a la victima y viceversam, aqui lo que hacemos es no enviarle paquetes a la victima lo que hace que se quede sin conexion.

Visualización de Resultados: La interfaz grafica como tal no tiene todavia un output de lo que va pasando cuando lanzamos el ataque pero la terminal si, van saliendo algunos mensajes actualizandonos de como va la cosa.

Consideraciones:

Es importante recordar que el uso de herramientas de análisis de red debe realizarse de manera ética y responsable. Esta aplicación es una demostración educativa y debe utilizarse únicamente en entornos donde tengas permiso para realizar pruebas de seguridad.



