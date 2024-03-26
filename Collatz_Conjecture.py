def steps(number:int):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    stps = 0
    for n in range(1, number):
        if number == 1:
            number = number
            break 
        elif number%2 == 0:
            number = number//2
        else:
            number = 3*number+1
        stps += 1
    return stps
