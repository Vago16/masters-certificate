from timeit import default_timer as timer
import sys

#
# Music Streaming Application
#

# This class is used to store one node in the linked list.
# A node has a song's title and three pointers to other nodes.
class Song:
    def __init__(self, title):
        self.title = title
        self.nextInOrigOrder = None # pointer to next song on list when initial list is created
        self.prevInPlaylist  = None # pointer to previous song in the user's playlist
        self.nextInPlaylist  = None # pointer to next song in the user's playlist

    # methods used to set the pointers
    def setNextInOrigOrder (self, node):
        self.nextInOrigOrder = node

    def setPrevInPlaylist (self, node):
        self.prevInPlaylist = node

    def setNextInPlaylist (self, node):
        self.nextInPlaylist = node

    # returns the song title of the node    
    def getSongTitle(self):
        return(self.title)

    # returns the next node (in the original order)
    def getNextInOrigOrder(self):
        return(self.nextInOrigOrder)

    # returns the previous node (in the playlist order)
    def getPrevInPlaylist(self):
        return(self.prevInPlaylist)

    # returns the next node (in the playlist order)
    def getNextInPlaylist(self):
       return(self.nextInPlaylist)



# Main Program
# Initializing pointers that will be used to create and traverse the linked list
headNodeOrig = None
headNodePlaylist = None
tailNodePlaylist = None
currentNode = None

# TO DO: write your code below this line.



