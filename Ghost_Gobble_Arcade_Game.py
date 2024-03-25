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
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    #Verify that Pac-Man has scored when a power pellet or dot has been eaten.
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    #Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    #Trigger the victory event when all dots have been eaten. 
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
