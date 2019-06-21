from multiprocessing import Pool
import os, random, time


def long_time_task(name):
    print('run long task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s is run %0.2f secends' % (name, (end - start)))

if __name__ == '__main__':
    print('pardents is %s' % os.getpid())
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


