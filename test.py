import threading
from time import time

import numpy as np


def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (nrows, ncols, n, m) where
    n * nrows, m * ncols = arr.shape.
    This should be a view of the original array.
    """
    h, w = arr.shape
    n, m = h // nrows, w // ncols
    return arr.reshape(nrows, n, ncols, m).swapaxes(1, 2)


def do_dot(a, b, out):
    out[:] = np.matmul(a, b)


# TODO  Revisar bien como funciona
def pardot(a, b, nblocks, mblocks, dot_func=do_dot):
    """ Return the matrix product a * b.
        The product is split into nblocks * mblocks partitions that are performed
        in parallel threads.
    """
    n_jobs = nblocks * mblocks
    print('running {} jobs in parallel'.format(n_jobs))

    out = np.empty((a.shape[0], b.shape[1]), dtype=a.dtype)

    out_blocks = blockshaped(out, nblocks, mblocks)
    a_blocks = blockshaped(a, nblocks, 1)
    b_blocks = blockshaped(b, 1, mblocks)

    threads = []
    for i in range(nblocks):
        for j in range(mblocks):
            th = threading.Thread(target=dot_func,
                                  args=(a_blocks[i, 0, :, :],
                                        b_blocks[0, j, :, :],
                                        out_blocks[i, j, :, :]))
            th.start()
            threads.append(th)

    for th in threads:
        th.join()

    return out


if __name__ == '__main__':
    a = np.random.rand(20000, 10000)
    b = np.random.rand(10000, 10000)

    start = time()
    np.matmul(a, b)
    time_par = time() - start
    print('matmul: {:.2f} seconds taken'.format(time_par))

    # start = time()
    # pardot(a, b, 2, 2)
    # time_par = time() - start
    # print('pardot: {:.2f} seconds taken'.format(time_par))
    #
    # start = time()
    # np.dot(a, b)
    # time_dot = time() - start
    # print('np.dot: {:.2f} seconds taken'.format(time_dot))
