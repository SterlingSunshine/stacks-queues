
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        self.buffer_size = INITIAL_QUEUE_SIZE
        self.front = -1
        self.rear = -1
        self.size = 0
      

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """

        # buffer is full
        if self.size == self.buffer_size:
            raise QueueFullException

        # buffer is empty and new
        if self.front == -1:
            print("Imma new buffer!")
            self.front = 0
            self.rear = 1
            self.store[self.front] = element
            self.size += 1
            return

        self.store[self.rear] = element
        self.rear = (self.rear + 1 ) % self.buffer_size
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        # queue empty
        if self.size == 0:
            raise QueueEmptyException

        element = self.store[self.front]
        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1

        return element

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.size == 0:
            return None

        return self.store[self.front]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        if self.size == 0:
            return True

        return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """

        return str([self.store[index % self.buffer_size] for index in range(self.front, (self.front + self.size))])