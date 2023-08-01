def steps(number:int):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    pasos = []
    stps = 0
    for n in range(1, number):
        if number == 1:
            nu = int(number)
            break 
        elif number%2 == 0:
            nu = int(number/2)
        else:
            nu = int(3*number+1)
        number = nu
        stps += 1

    return stps
