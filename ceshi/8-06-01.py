from multiprocessing import Process
import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
	print('i am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
	print('i (%s) just create a child process (%s).' % (os.getpid(), pid))
	