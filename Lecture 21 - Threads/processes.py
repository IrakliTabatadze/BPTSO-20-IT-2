import threading
import multiprocessing
from datetime import datetime
def worker(task_id):
    print(f'Processing Task: {task_id}')
    result = sum(i**2 for i in range(10000000))
    print(f'Finished Processing Task: {task_id}')

start_time = datetime.now()

# for i in range(1, 11):
#     worker(i)

threads = []
for i in range(1, 11):
    # thread = threading.Thread(target=worker, args=(i,))
    thread = multiprocessing.Process(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = datetime.now()

print(f'Finished All Task: {end_time - start_time}')