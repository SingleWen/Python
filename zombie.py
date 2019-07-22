
import os,sys

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    sys.exit(2)
else:
    """
    os.wait() 
    """
    pid,status = os.wait()
    print("pid:",pid)
    print("statis:",status) 

    while True:
        pass
