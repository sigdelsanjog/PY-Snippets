# Problem: Simulate the threading operation in Operating system which illustrates two threads
# running seperate process simultaneously
# IMPORT A MODULE
# CREATE A THREAD
# START THE THREADED OPERATION
# FINALLY JOIN THE THREADS TO STOP THE TASK AFTER ITS COMPLETION

import time
import threading


def get_process(processes):
    for person in processes:
        print("Currently running process is: " + person)
        time.sleep(0.5)
 
 
def assign_process_id(processes):
    id = 1
    for process in processes:
        print("The process id of Process: {} is {}:".format(process, id))
        id += 1
        time.sleep(0.5)
 
 
processes = ['Chrome', 'Firefox', 'Safari', 'Opera']
 
log_time = time.time()
 

first_thread = threading.Thread(target=get_process, args=(processes,))
second_thread = threading.Thread(target=assign_process_id, args=(processes,))
 

first_thread.start()
second_thread.start()
 

first_thread.join()
second_thread.join()
 

print("All Process Execution Completed with time:" + str(time.time() - log_time))
