import numpy as np

def multiple(prime_list, ubound):
    prime_list = list(prime_list)
    num_list = np.arange(1, ubound)
    idx = np.array([False]*(ubound-1))
    for x in prime_list:
        idx = np.bitwise_or(idx, (num_list%x==0))
        
    return num_list[idx].sum()
