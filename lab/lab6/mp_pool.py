from multiprocessing.pool import Pool 
from multiprocessing import cpu_count

def one_function(i):
    return i 

if __name__=='__main__':
    pool = Pool(cpu_count() - 1)
    # three tasks here 
    # map will collect return value into a list
    # with original order
    r = pool.map(one_function, (1, 'a', 0.5))
    print(r)
