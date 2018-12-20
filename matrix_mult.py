from time import time

import numpy as np


def matmul_cpu(a, b):
    """ Multiplica 2 matrices en CPU.

    :param a:
        Primera matriz.
    :param b:
        Segunda matriz.
    :return:
        Resultado de la multiplicación.
    """
    return np.matmul(a, b)


if __name__ == '__main__':

    m = np.random.rand(10000, 10000)
    delta = 0
    for i in range(0, 5):
        print(f"Multiplicando matrix {i}")
        start = time()
        matmul_cpu(m, m)
        delta += time() - start
    print('matmul: {:.3f} seconds taken'.format(delta / 5))
