# fork() : fork() is an operation whereby a process creates a copy of itself. It is usually a system call, implemented in the kernel.
# getpid() : getpid() returns the process ID (PID) of the calling process.
import os


def ParentProcess():
    for i in range(1,10):
        print("Parent Proc: %d", os.getpid())
    print("Parent process exiting")


def ChildProcess():
    for i in range(1,10):
        print("Child Proc: %d"%(i))
    print("Child process exiting")


# Fork and create a child process
retVal = os.fork()
print("Return value is %d"%(retVal))
if retVal is 0:
    ChildProcess()

else:
    ParentProcess()