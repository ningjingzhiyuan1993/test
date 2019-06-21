import os
from multiprocessing import Process

#print('Process (%s) start...' % os.getpid())

def run_proc(name):
    print('run child process is %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p1= Process(target=run_proc, args=('test1',))
    print('Child process will start.')
    p.start()
    p.join()
    p1.start()
    p1.join()
    print('end')