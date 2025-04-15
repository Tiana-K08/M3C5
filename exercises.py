# Cree un bucle For de Python.
fruits = ["apple", "banana", "cherry", "orange", "mango"]

for fruit in fruits:
  print(f"Fruit: {fruit}")

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def sum(a, b, c):
  return a + b + c


result = sum(20, 12, 4)
print(f"The sum is: {result}")

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
sum = lambda a, b, c: a + b + c


result = sum(20, 12, 4)
print(f"The sum is: {result}")

# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 
lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]
nombre = "Enrique"

if nombre in lista_nombre:
    print("El nombre coincide con uno en la lista.")
else:
    print("El nombre NO coincide con ninguno en la lista.")