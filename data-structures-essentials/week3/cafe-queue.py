class BobaShop:
    default_capacity = 10

    def __init__(self):
        self._data = [None] * BobaShop.default_capacity
        self._size = 0
        self._front = 0

    #returns length of the order list
    def __len__(self):
        print("The order list has {0} items waiting to be completed.".format(self._size))
        return(self._size)
    
    #returns the next item to be completed
    def peek(self):
        if self._size == 0:
            print("No orders are needing to be filled now.")
            return self._size
        else:
            order = self._data[self._front]
            print("The next order to be filled is {0}.".format(order))

    #checks if the queue is empty, and if not, returns length of the order list
    def is_empty(self):
        if self._size == 0:
            print("No orders are needing to be filled now.")
            return self._size
        else:
            len(self)

    #adds items to the order list if the list is not over capacity
    def enqueue(self, order):
        if self._size >= BobaShop.default_capacity:
            return ("The queue is full, cannot add more orders.")
        end = (self._front + self._size) % len(self._data)
        self._data[end] = order
        self._size += 1
        return print("{0} has been added to orders.".format(order))
    
    #signifies an order has been completed and removes the item from the list
    def dequeue(self):
        if self._size == 0:
            raise ("Order list is empty, cannot remove any items from the list.")
        order = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % BobaShop.default_capacity
        self._size -= 1
        print("The order of {0} has been completed.".format(order))

#intialize empty list
boba_shop = BobaShop()
boba_shop.is_empty()
boba_shop.enqueue("Taro Milk Tea")
boba_shop.enqueue("Matcha Latte")
boba_shop.is_empty()
boba_shop.peek()
boba_shop.dequeue()
boba_shop.dequeue()
boba_shop.peek()


