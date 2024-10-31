# Criptograma Decoder

**Programa para descifrar un criptograma**

Este programa es un minijuego diseñado para que el usuario descodifique un criptograma. Se compone de varios pasos:

1. El programa utiliza un archivo con texto aleatorio del cual extrae cada letra y le asigna un número aleatorio entre 1 y 27, asegurando que cada letra tenga un número único asociado.

2. Selecciona una palabra aleatoria del texto. Esta palabra revelará algunas letras iniciales en la matriz encriptada.

3. Para añadir nuevas letras, solicita al usuario seleccionar un número y asignarle una letra.

4. El programa verifica si el número está en la matriz encriptada y si la letra asociada aún no ha sido descubierta.

5. La matriz se actualiza mostrando los números seleccionados previamente y se registra la información del número y su letra en un diccionario.

6. Pregunta al usuario si está satisfecho con el cambio y repite el proceso desde el paso 3 en un bucle hasta descifrar todo el texto.

7. Si en algún momento el usuario desea cambiar un número que ha sido modificado previamente, el programa reemplazará el número por la nueva letra.

**EJEMPLO DE OUTPUT**

Palabra Aleatoria Descubierta: HOLA

```plaintext
25 12 18 9 █ 3 7 █ 18 18 9 3 12 █ 3 9 26 27 12 14
H  O  L  A █     █ L  L  A   O  █   A       O
16 20 7 █ 24 9 18

Enter the number to select:

* El primer Ouput es la matriz encriptada con las letras de la palabra aleatoria descubiertas. Y se pide al usuario que añada otra seleccionando el número a cambiar.
```
