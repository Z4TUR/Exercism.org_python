"""Functions used in preparing Guido's gorgeous lasagna. 
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
#TODO: define the 'EXPECTED_BAKE_TIME' constant.

EXPECTED_BAKE_TIME = 40
ptm = None
elapsed_bake_time = None
number_of_layers = 0
time = 0


def bake_time_remaining(time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_bake_time = int(EXPECTED_BAKE_TIME - time)
    return elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    :param ptm: 2 * number of layers.
    :return: ptm that come to the number of layers.
    """
    ptm = int(2 * number_of_layers)
    return ptm


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elapse time.
    :param etm: int - ptm + elapsed_bake_time.
    :return: int - etm that come to number of layer and elapse bake time'.
    """
    etm = (2 * number_of_layers) + elapsed_bake_time
    return etm
