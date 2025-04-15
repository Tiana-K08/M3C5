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

***¡Importante!*** En Python, la indentación (los espacios al inicio de la línea) es muy importante. El bloque de código dentro del **if** debe tener una vacío (normalmente 2 o 4 espacios).

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

# ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?
Los bucles son una de las herramientas fundamentales en la programación, que permiten ejecutar repetidamente un bloque de código varias veces. Esto es útil cuando se necesita procesar grandes volúmenes de datos (por ejemplo, recorrer los elementos de una lista o realizar cálculos varias veces). En Python existen dos tipos de bucles: **for** y **while**.

El bucle **for** es ideal para recorrer elementos de colecciones, mientras que el bucle **while** se utiliza para ejecutar código mientras se cumpla una condición determinada. Ambos bucles tienen sus particularidades, y es importante elegir el tipo de bucle adecuado según la tarea.

---
El bucle **for** se utiliza para recorrer elementos (por ejemplo, en una lista, cadena, conjunto o diccionario). Continúa mientras haya elementos por recorrer y se detiene automáticamente cuando llega al final del objeto.

Ejemplo:
```
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)

# apple
# banana
# cherry
```
En este ejemplo, el bucle **for** recorre cada elemento de la lista **fruits** y lo muestra en pantalla. No sabemos de antemano cuántos elementos hay en la lista, pero el bucle se detendrá automáticamente cuando los haya recorrido todos.

***¡Importante!*** Al igual que en las estructuras condicionales, los bloques de código dentro de los bucles deben tener vacío (normalmente de 2 o 4 espacios).

***¡Importante!*** Es una práctica común nombrar la variable del bloque en singular, basada en el nombre de la colección.

---
El bucle **while** ejecuta un bloque de código mientras la condición se mantenga verdadera. Esta condición se verifica antes de cada iteración. Si la condición se vuelve falsa, el bucle se detiene. Normalmente, en un bucle **while** se establece un contador de iteraciones (de lo contrario, el bucle puede volverse infinito). El punto en el que el bucle se detiene se llama valor de control.

El bucle **while** es útil cuando no se conoce de antemano la cantidad de iteraciones y el bucle debe continuar hasta que se cumpla una condición específica.

Ejemplo:
```
counter = 0

while counter < 5:
  print(counter)
  counter += 1

# 0
# 1
# 2
# 3
# 4
```
En este ejemplo, el bucle **while** se sigue ejecutando mientras la variable **counter** sea menor que **5**. Después de cada iteración, el valor de **counter** se incrementa en **1**, y cuando alcanza el valor **5**, la condición se vuelve falsa y el programa termina la ejecución del bucle.

***¡Importante!*** Si la condición siempre es verdadera (por ejemplo, **True**), el bucle será infinito. Por eso, es fundamental controlar cuidadosamente la condición en un bucle while para evitar errores.

Ejemplo:
```
counter = 10

while counter > 5:
  print(counter)
  counter += 1

# infinite loop
```
En este ejemplo, el bucle **while** se ejecutará infinitamente porque la condición **counter > 5** siempre es verdadera (**True**). Esto significa que Python continuará ejecutando el bloque de código dentro del bucle sin detenerse, sin verificar ninguna otra condición.

---
En Python, se pueden usar dos operadores para controlar la ejecución de los bucles: **break** (para salir del bucle si se alcanza un resultado determinado) y **continue** (para omitir la iteración actual y pasar a la siguiente).

El operador **break** se utiliza para salir del bucle de forma inmediata, sin importar cuántas iteraciones queden. Esto permite finalizar la ejecución del bucle si se cumple una condición específica.

Ejemplo:
```
usernames = [
  "Jon",
  "Tyrion",
  "Cersei",
  "Sansa",
]

for username in usernames:
  if username == "Cersei":
    print(f"{username} was found at index {usernames.index(username)}")
    break
  print(username)


# Jon
# Tyrion
# Cersei was found at index 2
```
Aquí, el bucle recorrerá uno por uno los nombres de la lista hasta que encuentre el nombre **"Cersei"**. En ese momento, gracias al operador **break**, finalizará su ejecución.

El operador **continue** omite el resto del código en la iteración actual del bucle y pasa directamente a la siguiente. Esto significa que, si dentro del bucle se ejecuta **continue**, todas las líneas de código restantes en el cuerpo del bucle se ignoran, y el ciclo continúa con la siguiente iteración.

Ejemplo:
```
usernames = [
  "Jon",
  "Tyrion",
  "Cersei",
  "Sansa",
]

for username in usernames:
  if username == "Tyrion":
    print(f"Sorry, {username}, you are not allowed")
    continue
  else:
    print(f"{username} is allowed")

# Jon is allowed
# Sorry, Tyrion, you are not allowed
# Cersei is allowed
# ansa is allowed
```
Aquí, el bucle recorre todos los elementos de la colección uno por uno. Cuando la condición **if** es verdadera (**True**), el ciclo no se detiene gracias al operador **continue**, sino que pasa al siguiente elemento de la lista y continúa hasta que se hayan recorrido todos los elementos.

# ¿Qué es una lista por comprensión en Python?
**List Comprehension** es una sintaxis especial en Python que permite crear listas a partir de otras colecciones en una sola línea de código.

Ejemplo: *Supongamos que tenemos una lista de números y queremos incrementar cada uno de ellos en 2.*
Sintaxis estándar:
```
numbers = [3, 5, 7, 2, 9, 6, 1, 8]
new_numbers = []

for number in numbers:
  new_numbers.append(number + 2)

print(new_numbers)

# [5, 7, 9, 4, 11, 8, 3, 10]
```
Sintaxis List Comprehension:
```
numbers = [3, 5, 7, 2, 9, 6, 1, 8]
new_numbers = [number + 2 for number in numbers]

print(new_numbers)

# [5, 7, 9, 4, 11, 8, 3, 10]
```
Esta sintaxis es más compacta y legible. En ambos casos, el resultado será el mismo.

Sin embargo, hay situaciones en las que no se recomienda utilizar List Comprehension:
- la lógica es demasiado compleja;
- la expresión es muy larga y se pierde la legibilidad;
- hay muchas condiciones o bucles anidados.
En esos casos, es mejor usar la sintaxis del bucle **for** tradicional.

# ¿Qué es un argumento en Python?
**Un argumento** en Python es un valor que se pasa a una función cuando se llama. Con la ayuda de los argumentos, podemos controlar el comportamiento de la función y proporcionarle datos para procesar.

Las funciones en Python pueden aceptar:
- argumentos posicionales;
- argumentos con nombre (keyword arguments);
- argumentos con valores predeterminados;
- una cantidad variable de argumentos (desempaquetado de argumentos).

---
**Los argumentos posicionales** son los argumentos más básicos. El orden en que se pasan es importante, es decir, los valores se pasan a la función en el mismo orden en que están definidos los parámetros.

Ejemplo:
```
def greet(first, last):
  print(f"Hi, {first} {last}!")


greet("Tetiana", "Kononenko")
# Hi, Tetiana Kononenko!

greet("Kononenko", "Tetiana")
# Hi, Kononenko Tetiana!
```
En este ejemplo, la forma en que se usan los argumentos introducidos se determina por su posición. El orden en el que pasamos los argumentos a la función es muy importante.

---
En funciones simples, es fácil y cómodo usar argumentos posicionales, pero cuando hay muchos argumentos, esto puede causar confusión.
Cuando se pasan más de dos argumentos a una función, es mejor usar **argumentos con nombre (keyword arguments)**. De esta manera, podemos especificar claramente la posición de cada argumento y evitar confusiones.

**Los argumentos con nombre** permiten indicar explícitamente a qué parámetro corresponde cada valor. Esto elimina la dependencia del orden.

Ejemplo:
```
def greet(first, last, status):
  print(f"Hi, {first} {last}! You are logged in as a {status}.")


greet("seller", "Tetiana", "Kononenko")
# Hi, seller Tetiana! You are logged in as a Kononenko.
# Aquí el orden de los argumentos depende de la posición y no se muestra correctamente

greet(status = "seller", first = "Tetiana", last = "Kononenko")
# Hi, Tetiana Kononenko! You are logged in as a seller.
# Aquí se utilizan argumentos con nombre y se muestran correctamente
```

---
Se puede establecer **un valor predeterminado** para los argumentos; así, al llamar a la función sin especificar dichos argumentos, se utilizará el valor predeterminado.

Ejemplo:
```
def greet(name = "guest"):
  print(f"Hello, {name}!")


greet()           # Hello, guest!
greet("Tetiana")  # Hello, Tetiana!
```

Si se utiliza un **objeto mutable** (por ejemplo, una lista) como valor predeterminado, este se conservará entre las llamadas a la función, lo que puede provocar errores.

Ejemplo:
```
def append_to_list(my_list = []):
  my_list.append(1)
  return my_list


print(append_to_list())  # [1]
print(append_to_list())  # [1, 1] — ¡de repente!
```

***¡Importante!*** Establecer listas como argumento predeterminado es una muy mala práctica, ya que las listas son mutables. Es mejor evitar este enfoque.

---
Para pasar una **cantidad variable de argumentos** a una función, se suele usar la palabra clave **\*args**. Esto permite pasar cualquier cantidad de argumentos, que serán recopilados en una tupla.

Se puede usar cualquier otro nombre (**\*nombre**), pero por convención general se utiliza **\*args**.

Ejemplo:
```
def sum_numbers(*args):
  print(sum(args))


sum_numbers(4, 2, 6)  # 12
```

Ejemplo de desempaquetado y unión en una sola cadena:
```
def my_fruits(*args):
  print(f"My favorite fruits are: {', '.join(args)}")


my_fruits("apple", "kiwi", "pear")
# My favorite fruits are: apple, kiwi, pear
```
En este ejemplo, los argumentos se desempaquetan y se imprimen en una sola línea gracias al método **.join()**.
Si se desempaquetan los argumentos sin este método, se mostrarán como una tupla común:
```
def my_fruits(*args):
  print(f"My favorite fruits are: {args}")


my_fruits("apple", "kiwi", "pear")
# My favorite fruits are: ('apple', 'kiwi', 'pear')
```

---
También se puede pasar a una función **una cantidad variable de argumentos con nombre** utilizando la palabra clave **\*\*kwargs** (convención ampliamente aceptada). Todos los argumentos con nombre se recopilan en un diccionario.

Ejemplo:
```
def greeting(**kwargs):
  print(f"Hi, {kwargs['first']} {kwargs['last']}, have a great day!")


greeting(first = "Tetiana", last = "Kononenko")
# Hi, Tetiana Kononenko, have a great day!
```

---
Una función puede aceptar diferentes tipos de argumentos al mismo tiempo. **El orden de los argumentos** en la definición de la función es el siguiente: posicionales, con nombre, \*args, \*\*kwargs.

Ejemplo:
```
def example(a, b = 0, *args, **kwargs):
  print(f"a = {a}, b = {b}, args = {args}, kwargs = {kwargs}")


example(1, 10, 5, 6, 15, 4, c = 10, d = 20,)
# a = 1, b = 10, args = (5, 6, 15, 4), kwargs = {'c': 10, 'd': 20}
```

***¡Importante!*** Los argumentos posicionales no pueden ser especificados después de los argumentos con nombre — esto es un error de sintaxis.

Ejemplo:
```
def example(a, b = 0, *args, **kwargs):
  print(f"a = {a}, b = {b}, args = {args}, kwargs = {kwargs}")


example(1, b = 10, c = 10, d = 20,)
# a = 1, b = 10, args = (), kwargs = {'c': 10, 'd': 20}
```

# ¿Qué es una función Lambda en Python?
# ¿Qué es un paquete pip?