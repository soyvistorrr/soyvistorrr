"""
def SonAmigos(x, y):
    suma_x = 0
    suma_y = 0

    for i in range(1, x):
        if x % i == 0:
            suma_x += i

    for i in range(1, y):
        if y % i == 0:
            suma_y += i

    if suma_x == y and suma_y == x:
        print(f"{x} y {y} son números amigos.")
        return True
    else:
        print(f"{x} y {y} no son números amigos.")
        return False
resultado = SonAmigos(382, 192)
print(f"Resultado: {resultado}\n")
"""
"""
def imprimirNumeros(n):
   for i in range(1 , n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

imprimirNumeros(20)
"""

def Digitos(n):
    for i 
