def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    numero = 1
    if number != 1:
        numero = 2       
        for n in range(2, number):
            numero = numero * 2
    return numero


def total():
    ttl = 1
    numero = 2
    for n in range(1, 64):
        ttl += numero
        numero = numero * 2
    return ttl
