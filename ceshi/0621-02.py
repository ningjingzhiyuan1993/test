from multiprocessing import Process, Queue
import os, time, random


def write_quene(q):
    print('write process is %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('write value is %s' % value)
        q.put(value)
        time.sleep(random.random())

def read_quene(f):
    print('read process is %s' % os.getpid())
    while True:
       value = f.get(True)
       print('read value is %s' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write_quene, args=(q,))
    pr = Process(target=read_quene, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()




