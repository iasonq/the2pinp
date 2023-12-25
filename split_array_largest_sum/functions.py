import numpy as np

def split(ar, k):
    s = np.size(ar)
    d, r = divmod(s, k)
    return n, d, r