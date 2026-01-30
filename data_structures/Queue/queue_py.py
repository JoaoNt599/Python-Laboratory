from queue import Queue

queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.qsize())
for i in range(3):
    print(queue.get())