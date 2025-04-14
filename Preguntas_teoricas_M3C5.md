# ¿Qué es un condicional?
Los condicionales permiten que los programas reaccionen de diferentes maneras ante distintas situaciones y se comporten de forma dinámica. Un programa puede ejecutar distintos bloques de código dependiendo de ciertas condiciones.

Se puede imaginar que el programa "pregunta":
"Si se cumple la condición y es verdadera, ¿qué debo hacer? ¿Y si es falsa, qué hago entonces?"
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

***¡Importante!*** En Python, la indentación (los espacios al inicio de la línea) es muy importante. El bloque de código dentro del **if** debe tener una sangría (normalmente 2 o 4 espacios).

---
A veces necesitamos que el programa ejecute dos instrucciones diferentes. La primera si la condición es verdadera (True) y la segunda si es falsa (False). En este caso, se utiliza la construcción **if / else**.

Ejemplo:
```
age = 5

if age > 18:
  print("¡Ya eres un adulto!")
else:
  print("¡Eres joven todavía!") # ¡Eres joven todavía!
```
Aquí, si la condición es verdadera (True), se ejecutará el bloque de código después de **if**, pero si la condición es falsa (False), entonces el programa ejecutará el bloque de código después de **else**.

---
Si necesitamos comprobar una condición más de dos veces, podemos añadir la construcción elif (abreviatura de "else if") y realizar tantas comprobaciones como necesitemos.

Ejemplo:
```
temperature = 25

if temperature < 0:
  print("Hace mucho frío")
elif temperature < 20:
  print("Hace fresco")
elif temperature < 30:
  print("Hace calor") # Hace calor
else:
  print("Hace mucho calor")
```
Aquí, las condiciones se verifican en cada bloque de forma secuencial hasta que se encuentra la primera afirmación verdadera. Primero se verifica el bloque **if**, y si la condición es verdadera (True), se ejecuta el bloque de código dentro y el programa sale de la estructura condicional. Si es falsa (False), el programa pasa a verificar la siguiente condición en el bloque **elif**. Este procedimiento de verificación se repite. Si ninguna condición es verdadera (True), entonces se ejecuta el bloque de código dentro del **else**.

---
Si es necesario asignar un valor a una variable dependiendo de una condición, se puede utilizar el **operador ternario**. Esta es una forma abreviada de la construcción **if/else**.

Ejemplo:
```
age = 14
status = "Mayor de edad" if age >= 18 else "Menor de edad"
print(status) # Menor de edad
```
***¡Importante!*** el operador ternario es conveniente, pero si la expresión se vuelve demasiado larga o confusa, es mejor usar un if normal. El código siempre debe permanecer legible.

---
A veces necesitamos comprobar varias condiciones al mismo tiempo. Para eso existen los operadores lógicos:
- and — ambas condiciones deben ser True
- or — al menos una de las condiciones debe ser True
- not — invierte (niega) la condición

Ejemplo:
```
age = 20
has_license = True

if age >= 18 and has_license:
  print("¡Puedes conducir!") # ¡Puedes conducir!
else:
  print("No puedes conducir.")
```
Ejemplo:
```
ticket_type = "estudiante"

if ticket_type == "jubilado" or ticket_type == "estudiante":
  print("¡Descuento aplicado!") # ¡Descuento aplicado!
else:
  print("Precio completo.")
```
Ejemplo:
```
name = ""

if not name:
  print("No ingresaste un nombre") # No ingresaste un nombre
else:
  print(f"¡Hola, {name}!")
```

De la misma manera, también podemos comprobar más de dos condiciones al mismo tiempo.

Ejemplo:
```
password = ""
face_id = False

if not password or not face_id:
  print("No se pudo verificar") # No se pudo verificar
else:
  print("Acceso autorizado")
```

***¡Importante!*** Python siempre evalúa las condiciones de izquierda a derecha.
Por eso, si hay varios operadores en una misma expresión, es mejor usar paréntesis para mayor claridad.

Ejemplo:
```
has_coupon = False
is_black_friday = True
total = 1200

if (has_coupon or is_black_friday) and total >= 1000:
  print("¡Descuento aplicado!") # ¡Descuento aplicado!
else:
  print("Descuento no disponible")
```

---
Las condiciones en Python suelen usar operadores de comparación. Lista de operadores de comparación en Python:

*(se utilizan para comparar números)*
- \> mayor que
- \>= mayor o igual que
- < menor que
- <= menor o igual que

*(se utilizan para comparar diferentes tipos de datos)*
- == igualdad
- != desigualdad

*(operador obsoleto)*
- <> desigualdad (Un operador obsoleto que no se debe usar, pero que aún puede encontrarse en programas antiguos. Este operador se utilizaba para comprobar la desigualdad entre números.)