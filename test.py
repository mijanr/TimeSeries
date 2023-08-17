import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate(
        **kwargs
):
    # return summation of all the arguments
    return sum(kwargs.values())


if __name__ == '__main__':
    dic = {'a': 1, 'b': 2, 'c': 3}
    print(calculate(**dic))