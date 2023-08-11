def equilateral(sides):
    if sides[0] == sides[1] == sides[2] and sides[0] > 0:
        return True
    else:
        return False
            

def isosceles(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        if sides[0] == sides[1] == sides[2]:
            return True
        elif sides[0] == sides[1] and sides[0] + sides[1] >= sides[2]:
            return True
        elif sides[0] == sides[2] and sides[0] + sides[2] >= sides[1]:
            return True
        elif sides[1] == sides[2] and sides[1] + sides[2] >= sides[0]:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[2] and sides[1] + sides[2] >= sides[0]:
                return True
            else:
                return False
        else:
            return False   
    else:
        return False

