import queue

# fifo 사용되는 큐 자료구조
data_queue = queue.Queue()

data_queue.put('a')
data_queue.put('b')

# print(list(data_queue.queue))
# print(data_queue.qsize())
# print(data_queue.get())
# print(data_queue.qsize())

q_lifo = queue.LifoQueue()
q_lifo.put(1)
q_lifo.put(2)

# 마지막에 넣은 요소가 나옴
# print(q_lifo.get())     

q_priority = queue.PriorityQueue()

# 데이터를 넣을 때 튜플로 넣음
q_priority.put((10, 'Park'))
q_priority.put((5, 1))
q_priority.put((15, 'Kim'))

# print(list(q_priority.queue))
# 우선순위가 가장 높은 것인 (5, 1)이 나옴
# print(q_priority.get())
# print(list(q_priority.queue))

q_list = list()

def enqueue(data):
    q_list.append(data)

def dequeue():
    data = q_list[0]
    del q_list[0]
    return data

for i in range(10):
    enqueue(i)

print(q_list)
print(dequeue())
print(q_list)

# for i in range(10):
#     dequeue()
#     print(q_list)





