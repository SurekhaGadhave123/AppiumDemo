import random

num = random.randint(1,9998)


def gen_random_mobno():
    rndm_mobno = str(num) + str(num) + str(num)[0:2]
    return rndm_mobno