#######################################################
# Threadings
#######################################################
import time
from datetime import datetime
import threading

def planning_project():
    time.sleep(3)
    print("Planning")


def start_project():
    time.sleep(4)
    print("Starting")


def get_ready():
    time.sleep(5)
    print("Ready")


start_time = datetime.now()

# planning_project()
# start_project()
# get_ready()



planning = threading.Thread(target=planning_project)
starting = threading.Thread(target=start_project)
ready = threading.Thread(target=get_ready)


planning.start()
starting.start()
ready.start()

print(threading.enumerate())

planning.join()
starting.join()
ready.join()

print(threading.enumerate())


end_time = datetime.now()

print(end_time - start_time)




#######################################################
# Thread Attributes
#######################################################

import threading
import random
import time


def worker(task_id):
    computation_time = random.randint(1, 5)
    print(f'Task {task_id} Started... Computation time: {computation_time}')

    time.sleep(computation_time)

    print(f'Task {task_id} Completed')


tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5']


threads = []

for task in tasks:
    thread = threading.Thread(target=worker, args=(task,))
    thread.start()
    threads.append(thread)


print(threading.enumerate())
print(threading.active_count())
for thread in threads:
    thread.join()

print('All Threads Finished')



#######################################################
# Thread Queue
#######################################################

import threading
import time
from queue import Queue


def worker(queue):
    while True:
        task = queue.get()

        if task is None:
            break

        print(f'Worker processing task: {task}')
        time.sleep(2)

        queue.task_done()
        print(f'Finished Task: {task}')


task_queue = Queue()

num_threads = 3
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=worker, args=(task_queue,))
    thread.start()
    threads.append(thread)


tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5']
for task in tasks:
    task_queue.put(task)

task_queue.join()

for _ in range(num_threads):
    task_queue.put(None)


for thread in threads:
    thread.join()
