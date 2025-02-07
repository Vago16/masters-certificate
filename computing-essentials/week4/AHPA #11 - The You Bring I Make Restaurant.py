# AHPA #11 - The "You Bring, I Make" Restaurant

# If my customers bring me a cow, I 
# make hamburgers. 
# If they bring me a chicken, I make nuggets. 
# If they bring me a pig, I make 
# bacon.
# If they bring me red grapes, I 
# make red wine. 
# If they bring me white grapes, I 
# make white wine.
# If they bring me carrots, I make 
# stew. 
# If they bring me potatoes, I make 
# mashed potatoes. 
# If they bring me apples, I make 
# apple pie.
#
# Create a program that will tell 
# me what to create based on what 
# my customer has brought to me.
#
# Student Name: Evagelos Petropoulos
#
#input to put as an argument to call for in the function later on
thing_to_bring = input('What are you bringing to The "You Bring, I Make" Restaurant" today? ').lower()      #not case sensitive

def restaurant(bring):      #bring is the arguments of what is entered
    if (bring == 'cow'): make = 'hamburgers'        #make is what can be made from the entered val
    elif (bring == 'chicken'): make = 'nuggets'
    elif (bring == 'pig'): make = 'bacon'
    elif (bring == 'red grapes'): make = 'red wine'
    elif (bring == 'white grapes'): make = 'white wine'
    elif (bring == 'carrots'): make = 'stew'
    elif (bring == 'potatoes'): make = 'mashed potatoes'
    elif (bring == 'apples'): make = 'apple pie'
    else:       #if not a correct input, return this asking user to try again, and add value for make so function works in all scenarios
        make = 'nothing'
        print('We can not make anything with that, please choose from our menu.')
    
    return ('You brought {0} so we made {1}.'.format(bring,make))

print(restaurant(thing_to_bring))       #prints out function

