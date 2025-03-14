# Función para verificar si un número es primo
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Función para obtener los primeros 10 números primos
def primeros_primos(cantidad):
    primos = []
    num = 2  # El primer número primo
    while len(primos) < cantidad:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos

# Llamada a la función para obtener los primeros 10 números primos
primos = primeros_primos(10)
print(primos)
