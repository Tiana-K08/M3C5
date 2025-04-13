# ¿Qué es un condicional?
Los condicionales permiten que los programas reaccionen de diferentes maneras ante distintas situaciones y se comporten de forma dinámica. Un programa puede ejecutar distintos bloques de código dependiendo de ciertas condiciones.

Se puede imaginar que el programa "pregunta":
"Si se cumple la condición y es verdadera (True), ¿qué debo hacer? ¿Y si es falsa (False), qué hago entonces?"
Dependiendo de la respuesta, se ejecuta un bloque de código específico.

Cualquier condición en Python se evalúa como True (verdadero) o False (falso).
Las condiciones bien escritas hacen que el código sea flexible e inteligente.
Esta es una de las habilidades más importantes de un programador.

---

La forma más simple de comprobar una condición y ejecutar un código solo si esa condición es verdadera (True) es usando la palabra clave **if**.

Ejemplo:
```
age = 20

if age > 18:
  print("¡Ya eres un adulto!")
```
Primero se crea una variable llamada **age** y se le asigna el valor **20**. Luego, después de la palabra clave **if**, se escribe la condición **age > 18**. Si el resultado de la condición es verdadero (True), se ejecuta el código dentro del bloque **if**. Si el resultado es falso (False), el código dentro del bloque **if** simplemente se omite, y el programa continúa con la siguiente parte.

***¡Importante!***
En Python, la indentación (los espacios al inicio de la línea) es muy importante.
El bloque de código dentro del if debe tener una sangría (normalmente 2 o 4 espacios).

***

A veces necesitamos que el programa ejecute dos instrucciones diferentes. La primera si la condición es verdadera (True) y la segunda si es falsa (False). En este caso, se utiliza la construcción if / else.

Ejemplo:
```
age = 5

if age > 18:
  print("¡Ya eres un adulto!")
else:
  print("¡Eres joven todavía!") # ¡Eres joven todavía!
```
Aquí, si la condición es verdadera (True), se ejecutará el bloque de código después de if, pero si la condición es falsa (False), entonces el programa ejecutará el bloque de código después de else.

___