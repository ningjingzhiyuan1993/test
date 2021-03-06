import time, threading

def loop():
    print('threading %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('threading %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('threading %s is end' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,)
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)