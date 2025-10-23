from multiprocessing import Process 
import time 


# use process class 
def one_process(name):
    for i in range(10):
        print(name, i)
        time.sleep(0.5)


if __name__=='__main__':
    # create a sub process
    p = Process(target=one_process, args=('In sub process',))
    p.start()
    time.sleep(0.2)
    for i in range(5):
        print('In main process', i)
        time.sleep(1)
    # wait for p to finish 
    p.join()
