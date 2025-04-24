from timeit import default_timer as timer
import sys

#start timer
start = timer()


####Hash Table Class####

class HashTable:
    def __init__(self, size = 29, a = 31):
        self.size = size        #given table sie
        self.a = a      #constant for hash function
        self.table = [""] * self.size

    def __len__(self):
        return self.size

    def hash_function(self, key):
        return hash(key) % self.size

    #insert values into hash table
    def insert(self, key):
        index = self.hash_function(key)
        orig_index = index      #index before insertion
        i = 0

        while self.table[index] not in ("", key):
            index = (index + 1) % self.size
            i += 1

            if index == orig_index:
                raise Exception("Table is full.")
            
        if self.table[index] == "":
            self.table[index] = key
            #uncomment to make sure insert is working correctly
            ##print("inserted {}".format(index))

    #print hash table for testing
    def display(self):
        i = 0
        while i < self.size:
            if self.table[i] != "":
                print("Index {1}: {0}".format(self.table[i], i))
            i += 1

    #obtain the hash code for a given word
    def _poly_hash_code(self, key):
        n = len(key)
        mask = ( 1 << 32 ) - 1      #limits to 32 bit ints
        h = 0       #initialize hash code
        for char in range(n):
            h = ( h << 5 & mask ) | ( h >> 27 )     #5 bit cyclic shift
            h += ord(key[char]) * (self.a ** (n - 1 - char))
        return h

    #division method as the compression function
    def hash_function(self, key):
        return self._poly_hash_code(key) % self.size
    
    #checks if word from second file exists in the hash table
    def contains(self, key):
        index = self.hash_function(key)
        orig_index = index 

        while self.table[index] != "":
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
            if index == orig_index:
                break
        return False

    def get_keywords(self):
        keywords = []
        for word in self.table:
            if word != "":
                keywords.append(word)
        return keywords


#command line arguments
if len(sys.argv) != 3:
    raise ValueError('Please provide two file names.')
firstFile = sys.argv[1]
secondFile = sys.argv[2]
print("\nThe hash table will be built from:", firstFile)
print("\nThe hash table will be compared to:", secondFile)

#open and read first file, and build hash table
first = open(firstFile,"r")	#open provided text file
firstList = first.readlines()	#read all lines in text file
first.close()	

#initialize first hash table
hash_table = HashTable()

for line in firstList:
    words = line.strip().lower().split()
    for word in words:
        hash_table.insert(word)

#open and read second file
second = open(secondFile,"r")	#open provided text file
secondList = second.readlines()	#read all lines in text file
second.close()	

#initialize the number of lines to be read and later displayed
num_lines = 0

#initialize dict to store words and frequency used
keyword_frequencies = {}

#get list of keywords(words that appeared in first file to compare against the second file)
keywords = hash_table.get_keywords()

for keyword in keywords:
    keyword_frequencies[keyword] = 0

#initialize the number of words to be read and later displayed
num_words = 0

for line in secondList:
    num_lines += 1
    words = line.strip().lower().split()
    for word in words:
        num_words += 1
        if hash_table.contains(word):
            keyword_frequencies[word] += 1

print()
print("**********************")
print("***** Statistics *****")
print("**********************")
print("Break down by keyword:")
print()
#loop through and print out the keywords and frequencies
for keyword in hash_table.get_keywords():
    print("{0} : {1}".format(keyword_frequencies[keyword], keyword))
print("Total lines read: {0}".format(num_lines))
print("Total words read: {0}".format(num_words))
#end timer
end = timer()
#print program runtime
print("Total Time of Program:", (end - start) * 1000, "milliseconds")

