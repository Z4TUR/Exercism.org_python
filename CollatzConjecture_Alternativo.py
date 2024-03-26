### Esta forma de solucionar el ejercicio Collatz Conjecture por alguna razon no es adminita en Exercism pero tambien es valida
def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    n = 0
    while number != 1:
        if number%2 == 0:
            number = number//2
        else:
            number = 3*number + 1
        n = n + 1
    return n 
