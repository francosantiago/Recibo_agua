"""PROGRAMA PARA
CALCULAR EL COSTO DEL RECIBO DEL AWA"""

print("-------------------------")
print("------Coste del agua-----")
print("-------------------------")

x = int(input("Ingrese la cantidad en mt3: "))

if x < 50:
    z = 10000
elif x >= 50 and x <= 200:
    z = 10000 + (2000 * (x - 50))
elif x > 200:
    z = 10000 + (3000 * (x - 50))

print("El valor del recibo es de " + str(z) + " pesos")