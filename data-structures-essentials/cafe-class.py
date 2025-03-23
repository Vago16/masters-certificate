#initialize empty list
cafes = []

class Cafe:
    def __init__(self, name, signature_drink, location, open, times_visited):
        self.name = name
        self.signature_drink = signature_drink
        self.location = location
        self.open = open
        self.times_visited = times_visited

    def __str__(self):
        return("The cafe {0} is located at {1} and features {2} as their signature drink.".format(self.name, 
                                                                                                  self.location, self.signature_drink))

    #this built-in function is necessary for the classes to be printed in the list in human readable format
    def __repr__(self):
        return self.name
    
    #checks if cafe is open and if it is returns open, if not, changes to open and returns it
    def is_open(self):
        if self.open == "open":
            return("{0} is now {1}.".format(self.name, self.open))
        else:
            self.open = "open"
            return("{0} is now {1}.".format(self.name, self.open))
    #checks if cafe is close and if it is returns closed, if not, changes to closed and returns it
    def is_closed(self):
        if self.open == "closed":
            return("{0} is now {1}.".format(self.name, self.open))
        else:
            self.open = "closed"
            return("{0} is now {1}.".format(self.name, self.open))
    #increments to the times_visited counter    
    def visit(self):
        self.times_visited += 1
        return("You have gone to {0} {1} times.".format(self.name, self.times_visited))

    
#initialize some cafe objects
chewy_boba = Cafe("Chewy Boba", "Chai Milk Tea with Boba", "University Square Plaza", "open", 100)
moge_tee = Cafe("Moge Tee", "Creme Brulee Milk Tea with Boba", "West of USF", "closed", 50)
starbucks = Cafe("Starbucks", "Pink Drink", "Bruce B Downs", "open", 2)

#append objects and print list
cafes.append(chewy_boba)
cafes.append(starbucks)
cafes.append(moge_tee)
print(cafes)

#test out some class functions
print(moge_tee.is_open())
print(moge_tee.is_closed())
print(chewy_boba.__str__())
print(chewy_boba.visit())


'''Whether I am studying at the moment or not, I love visiting cafes, especially ones that have boba.  I thought I would make a small class to store different cafes, their signature drink(honestly I just chose placeholders for this exercise), and whether or not they are open(which could be more helpful with more advanced code, but this is more a test of concept). 

My methods are pertaining to whether the cafe is open or closed right now, and will change it to open if not already, or closed if not already closed, depending on the class function called.  I found that adding in the __repr__ function helped a lot with the classes being viewable in list format when being printed, otherwise I would just be greeted with properties of the class.  I do not think the data needs to be stored in sorted order as appending new cafes or popping/removing existing ones would once again make the list in an unsorted state again.  I also had some difficulty sorting the list with the class objects inside myself and could not yet come to a conclusion as to how I could do it myself.



'''