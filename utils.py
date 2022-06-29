from random import randint


def random_value(probability):
    """
    Returns 0 if the random value / max value < probability, else returns 1
    :param probability: probability that the value returned is 0
    :return: 0 or 1
    """
    value = randint(0, 9)
    if value/10 >= probability:
        return 0
    else:
        return 1