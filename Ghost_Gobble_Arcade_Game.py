#Functions for implementing the rules of the classic arcade game Pac-Man.
'''
In this exercise, you need to implement some rules 
from Pac-Man, the classic 1980s-era arcade-game.
You have four rules to implement, all related to 
the game states.
Do not worry about how the arguments are derived, 
just focus on combining the arguments to return 
the intended result.
'''

def eat_ghost(power_pellet_active, touching_ghost):
    #Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
    return power_pellet_active is True and touching_ghost is True

def score(touching_power_pellet, touching_dot):
    #Verify that Pac-Man has scored when a power pellet or dot has been eaten.
    return touching_power_pellet is True or touching_dot is True


def lose(power_pellet_active, touching_ghost):
    #Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.
    return power_pellet_active is False and touching_ghost is True



def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    #Trigger the victory event when all dots have been eaten. 
    return has_eaten_all_dots is True and lose(power_pellet_active, touching_ghost) is False
