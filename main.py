import numpy
import random
arr = numpy.array([22,24,64, 63, 94, 6])

pyscript.write("output", f"{arr}")

def shuffle_array(*args):
    # shuffle = sorted(arr, key=lambda k:random.random())
    shuffle = random.choice(arr)
    pyscript.write("output", 20/7)