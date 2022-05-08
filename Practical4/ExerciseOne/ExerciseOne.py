class Empty(Exception):
    pass
class Full(Exception):
    pass

class QueueNormal():
    def __init__(self):
        self._queue = []
        
    def enqueue(self, e):
        self._queue.append(e)
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        self._queue.pop(0)
    def first(self):
        return self._queue[0]
    def is_empty(self):
        return len(self._queue) == 0
    def __len__(self):
        return len(self._queue)



class QueueRound():
    def __init__(self, length):
        self._queue = [None]*length
        self._frontQueueIndex = 0
        self._backQueueIndex = 0
        self._length = length
    def enqueue(self, e):
        if self._backQueueIndex !=0 and (self._backQueueIndex % self._length == self._frontQueueIndex % self._length):
            raise Full('the back of the queue reached the front')
        self._queue[self._backQueueIndex % self._length ] = e;
        self._backQueueIndex +=1
    def dequeue(self):
        if self._queue[self._frontQueueIndex] == None:
            Empty('The queue is empty')
        self._queue[self._frontQueueIndex % self._length] = None
        self._frontQueueIndex +=1
    def first(self):
        if self._queue[self._frontQueueIndex] == None:
            raise Empty('Queue is empty')
        return self._queue[self._frontQueueIndex]
    def is_empty(self):     
        return len(list(filter(None, self._queue))) == 0
    def __len__(self):
        return len(list(filter(None, self._queue)))
    def show(self):
        print(self._queue)


class DequeueRound():
    def __init__(self, length):
        self._queue = [None]*length
        self._frontQueueIndex = 0
        self._backQueueIndex = 0
        self._length = length
    def add_last(self, e):
        if self._backQueueIndex !=0 and (self._backQueueIndex % self._length == self._frontQueueIndex % self._length):
            raise Full('the back of the queue reached the front')
        self._queue[self._backQueueIndex % self._length ] = e;
        self._backQueueIndex +=1
    def add_first(self, e):
        if self._backQueueIndex !=0 and (self._backQueueIndex % self._length == self._frontQueueIndex % self._length):
            raise Full('the front of the queue reached the back')
        self._queue[(self._frontQueueIndex - 1) % self._length ] = e;
        self._frontQueueIndex -=1
    def delete_first(self):
        if self._queue[self._frontQueueIndex] == None:
            Empty('The queue is empty')
        self._queue[self._frontQueueIndex % self._length] = None
        self._frontQueueIndex +=1
    def delete_last(self):
        if self._queue[self._frontQueueIndex] == None:
            Empty('The queue is empty')
        self._queue[self._backQueueIndex - 1 % self._length] = None
        self._backQueueIndex -=1

    def first(self):
        if self._queue[self._frontQueueIndex] == None:
            raise Empty('Queue is empty')
        return self._queue[self._frontQueueIndex]
    def last(self):
        if self._queue[self._backQueueIndex] == None:
            raise Empty('Queue is empty')
        return self._queue[self._backQueueIndex]
    def is_empty(self):     
        return len(list(filter(None, self._queue))) == 0
    def __len__(self):
        return len(list(filter(None, self._queue)))
    def show(self):
        print(self._queue)



if __name__ == '__main__':
    Q = QueueNormal()
    Q.enqueue(5)
    Q.enqueue(7)
    print(len(Q))
    Q.enqueue(10)
    Q.dequeue()
    Q.dequeue()

    print(Q.first())

    print("-----------------------------")

    QR = QueueRound(10)
    print(QR.is_empty())
    QR.enqueue(1)
    QR.show()
    QR.enqueue(2)
    QR.enqueue(3)
    QR.enqueue(4)
    QR.enqueue(5)
    QR.enqueue(6)
    QR.enqueue(7)
    QR.enqueue(8)
    QR.enqueue(9)
    QR.enqueue(10)
    QR.dequeue()
    QR.enqueue(11)

    

    
    print(QR.is_empty())
    print(len(QR))
    QR.show()


    print("---------------------------------  ")

    D = DequeueRound(10)
    D.add_last(4)
    D.show()
    D.add_first(1)
    
    D.add_first(1)
    D.add_first(1)
    D.add_first(1)
    D.add_first(1)
     
    D.add_first(1)
    D.add_first(1)
    D.show()
    D.delete_first()
    D.delete_last()
    D.delete_last()
    

    D.show()

