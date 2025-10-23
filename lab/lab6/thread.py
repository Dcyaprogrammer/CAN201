from threading import Thread
import time 

def one_thread(name):
    for i in range(10):
        print(name, i)
        time.sleep(0.5)

if __name__=='__main__':
    p = Thread(target=one_thread, args=('In thread',))
    p.start()
    time.sleep(0.2)
    for i in range(5):
        print('In main process', i)
        time.sleep(1)
    p.join()
