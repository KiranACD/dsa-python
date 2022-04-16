class Queue:

    def __init__(self, cap = 5):
        self.arr = [0 for _ in cap]
        self.front = 0
        self.rear = 0
        self.capacity = cap
        self.size = 0
    
    def enque(self, x):

        if self.size < self.capacity:
            self.arr[(self.rear+1)%self.capacity] = x
            self.rear += 1
            self.rear = self.rear%self.capacity
            self.size += 1
        else:
            print(f'Size of queue = {self.size} is at capacity = {self.capacity}')
    
    def deque(self):
        
        if self.size > 0:
            self.front += 1
            self.front %= self.capacity
            self.size -= 1
        else:
            print('Queue is empty')
    
    def get_front(self):

        if self.size != 0:
            return self.arr[self.front]
    
    def is_queue_empty(self):

        return self.size == 0
    
    def print_queue(self):

        print(self.queue)
    
    


