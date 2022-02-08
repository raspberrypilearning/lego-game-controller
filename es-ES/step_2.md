## Utilización de los codificadores de motor LEGO® Spike ™

Los codificadores de motor no solo pueden girar, también pueden detectar con precisión cuántos grados han girado.

![Motor con la marca en forma de chupachup en línea con un círculo.](images/aligned_symbols.jpg)

Todos los motores LEGO® Spike ™ tienen codificadores. Si observas la parte del disco giratorio del motor, verá una marca con forma de chupachup que se puede alinear con la marca 0 en el cuerpo blanco del motor. Este es el codificador ajustado a cero grados y cualquier movimiento angular del eje del motor puede medirse en relación con este punto.

--- collapse ---
---
title: Cómo funcionan los codificadores de motor
---

Un codificador de motor, también llamado codificador rotativo o de eje, es un dispositivo electromecánico que le permite registrar la posición angular o el movimiento del eje. Normalmente lo hace convirtiendo la posición angular en una salida analógica o digital.

Si un motor tiene un codificador, eso significa que puedes establecer con mucha precisión la posición del eje. También te permite usar el motor como un dispositivo de entrada de manera que si algo cambia la posición del eje, se pueda detectar y usar para activar otras acciones en un programa de ordenador.

--- /collapse ---

--- task ---

Conecta un monitor, teclado y ratón a tu Raspberry Pi.

Conecta tu Build HAT a tu Raspberry Pi con el logotipo impreso hacia arriba, asegurándote de cubrir correctamente todos los pines.

Por último, conecta la energía; ya sea a través del conector de barril Build HAT o el puerto USB-C en la Raspberry Pi.

--- /task ---

--- task ---

Conecta un motor al puerto A del Build HAT.

![Motor conectado mediante un cable plano al puerto A en el build HAT.](images/motor_attached.jpg)

--- /task ---

--- task ---

Conecta una rueda grande al motor con cuatro clavijas de conexión. Gira la rueda para que la marca con forma de chupachup esté alineada con el cero.

![Motor con clavijas de conexión instaladas.](images/motor_with_pegs.jpg) ![Motor con rueda grande instalada.](images/motor_with_wheel.jpg)

--- /task ---

--- task ---

Abre Thonny desde el menú **Programación** de Raspberry Pi y haz clic en el **Shell** en la parte inferior de la ventana.

--- /task ---

--- task ---

Primero, importa la biblioteca Build HAT.

```python
from buildhat import Motor
```
Presiona Entrar.

--- /task ---

--- task ---

Luego, crea un objeto motor que le diga a Python que el motor está conectado al puerto `A`. Escribe:

```python
motor_izquierda = Motor ('A')
```
Presiona Entrar. (Habrá un ligero retraso, ¡ten paciencia!)

--- /task ---

--- task ---

Ahora, puedes pedirle al motor que informe su posición **absoluta**. Esta siempre estará entre `-180` y `180`.

```python
motor_izquierda.get_aposition()
```

Dependiendo de qué tan bien colocaste el motor al inicio, deberías obtener un valor cercano a `0`.

Mueve el motor y escribe la línea por segunda vez, y observa cómo cambia el valor.

--- /task ---

--- task ---

También puedes seguir la posición **relativa**. Esto es lo lejos que se ha movido desde el momento en que se inicia el programa, por lo que aumentará o disminuirá en `360` por cada giro de la rueda.

```python
motor_izquierda.get_position()
```
--- /task ---

--- task ---

Mueve el motor y verifica las posiciones absolutas y relativas, para comprender cómo cambian los valores.

--- /task ---


