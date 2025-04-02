#
# Capital Gain Calculator using Queues
#

from timeit import default_timer as timer
import sys

# ---- Class Empty Exception (since it is not defined in the original file) ---- #
class Empty(Exception):
    pass

# ---- Class ArrayQueue (mostly from textbook, code fragments 6.6 and 6.7) ---- #
# ---- You do not need to modify this class. ---- #
class ArrayQueue:
	"""FIFO queue implementation using a Python list as underlying storage."""
	DEFAULT_CAPACITY = 10 # moderate capacity for all new queues
	
	def __init__(self):
		"""Create an empty queue."""
		self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
		self.size = 0
		self.front = 0

	def len(self):
		"""Return the number of elements in the queue."""
		return self.size

	def is_empty(self):
		"""Return True if the queue is empty."""
		return self.size == 0

	def first(self):
		"""Return (but do not remove) the element at the front of the queue.
		Raise Empty exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty') 
		return self.data[self.front]

	def dequeue(self):
		"""Remove and return the first element of the queue (i.e., FIFO).
		Raise Empty exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty')
		answer = self.data[self.front]
		self.data[self.front] = None    	# help garbage collection
		self.front = (self.front + 1) % len(self.data)
		self.size -= 1
		return answer

	def enqueue(self, e):
		"""Add an element to the back of queue."""
		if self.size == len(self.data):         # if queue is full
			self.resize(2 *len(self.data))	# double the array size
		avail = (self.front + self.size) % len(self.data)
		self.data[avail] = e
		self.size += 1

	def resize(self, cap):	
		"""Resize to a new list of capacity >= len(self)."""
		old = self.data 			# keep track of existing list
		self.data = [None] * cap 		# allocate list with new capacity
		walk = self.front
		for k in range(self.size):		# only consider existing elements
			self.data[k] = old[walk]	# intentionally shift indices
			walk = (1 + walk) %len(old)	# use old size as modulus
		self.front = 0				# front has been realigned

	def replace_first(self, e): 
		"""Update the element at the front of the queue. """
		if self.is_empty():
			raise Empty('Queue is empty')
		self.data[self.front] = e

# -------- Main Program -------- #
# ----- Add your code here ----- #

# TO DO: start timer.
start = timer()


# TO DO: Parse the command line arguments.
if len(sys.argv) != 2:
	raise ValueError('Please provide one file name.')
inputFileName = sys.argv[1]

print("**********************")
print("The file that will be used for input is:", inputFileName)
print("**********************")
print("\n")	#space to match the output shown in the example output

# DONE: Initialize a queue named q. Use this queue to store the "buy" transactions.
q = ArrayQueue()

# DONE: Initialize a variable to keep track of the overall capital gain.
totalGain = 0

# TO DO: Read text file. Each line is a "transaction".
#        For each transaction, update the queue (add, update, or remove elements).
#        For transactions of type "sell", print the capital gain for that transaction.

f = open("transactions.txt","r")	#open provided text file
myList = f.readlines()	#read all lines in text file
f.close()	

for line in myList:
	line = line.strip()	#remove whitespace and newline characters
	parts = line.split()	#splits line further to make grabbing relevant values simpler, now is a list of each 'part' of the string	

	if (parts[0] == 'buy'):
		shares_to_buy = int(parts[1])	#num shares to buy
		buy_price = int(parts[4][1:])	#price of shares
		q.enqueue((shares_to_buy,buy_price))
		print("buy: " + str(shares_to_buy) + " at $" + str(buy_price))
	elif (parts[0] == 'sell'):
		shares_to_sell = int(parts[1])	#num shares to sell
		sell_price = int(parts[4][1:])	#price of shares
		print("sell: " + str(shares_to_sell) + " at $" + str(sell_price))
		capital_gain = 0	#initialize variable to hold capital gains

		while (shares_to_sell > 0):
			#gets first(oldest) shares and price that the shares were bought at
			#uses first() instead of dequeue to prevent issues with order
			shares_bought, price_bought = q.first()

			#sell all shares from oldest transaction if it is less than or equal to what the amount that is being sold is
			if (shares_bought <= shares_to_sell):
				capital_gain = capital_gain + (shares_bought * (sell_price - price_bought)) #increment the value by the amount of shares bought times the difference of the selling and buying price
				shares_to_sell -= shares_bought		#decrement value by the amount of shares bought that were just calculated to capital_gain
				q.dequeue()	#remove first item from queue as the transaction has been exhausted
			else:	#if greater, then only sell part of shares
				capital_gain = capital_gain + (shares_to_sell * (sell_price - price_bought))
				new_share_amount = shares_bought - shares_to_sell	
				q.replace_first((new_share_amount, price_bought))		#replaces first item instead of enqueue() to keep order intact
				shares_to_sell = 0 #no more shares to sell
		
		totalGain += capital_gain	#increment totalGain
		print("This transaction's capital gain is:", capital_gain, "\n")


		
# DONE: After processing the file, print the total capital gain for the entire sequence.
print("**********************")
print("The total capital gain is:", totalGain)
# TO DO: Print remaining elements in the queue.
print("\n**********************")
print("Shares remaining in the queue:")
while not q.is_empty():
    shares, price = q.dequeue()
    print("{0} shares bought at ${1} per share.".format(shares, price))



# TO DO: end timer.
end = timer()


# TO DO: Print program's runtime. 
print("\n************************")
print("Total Time of Program:", (end - start) * 1000, "milliseconds")


