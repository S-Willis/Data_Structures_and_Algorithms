class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,v):
        self.queue.append(v)

    def dequeue(self):
        popee = self.queue[0]
        self.queue.pop(0)
        return popee

if __name__ == '__main__':
    print("Test Queue")
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    print(q.queue)
    print(q.dequeue())
    print(q.queue)
