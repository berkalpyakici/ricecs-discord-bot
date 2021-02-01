import math
import random

def create_unique_auth():
    """
    Create 9 digit authentication code (3-3-3)
    """
    auth = ''
    for i in range(1, 10): 
        auth += str(math.floor(random.random() * 10))

        if i % 3 == 0:
            auth += "-"

    return auth[:-1]