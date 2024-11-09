# import collections
# from collections import deque
#
# deque_obj = deque()
#
# deque_obj.append(25)
# deque_obj.append(30)
# deque_obj.append(15)
# deque_obj.append(10)
# deque_obj.append(50)
#
# print(deque_obj.pop())
# print(deque_obj.pop())
# print(deque_obj.pop())
# print(deque_obj.pop())

# deque_obj.appendleft(100)
# deque_obj.appendleft(200)
# deque_obj.appendleft(300)
# print(deque_obj)
#
# print(deque_obj.popleft())
# print(deque_obj.popleft())


########################################################
# Queue
########################################################

from queue import Queue

q = Queue(maxsize=3)
print(f'Empty: {q.empty()}')
print(f'Queue Size: {q.qsize()}')

q.put('a')
q.put('b')
q.put('c')
print(f'Full: {q.full()}')
print(f'Queue Size: {q.qsize()}')
q.put_nowait('d')


print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(f'Queue is empty: {q.empty()}')
# q.put('e')
print(q.get_nowait())


