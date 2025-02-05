# AHPA #3 - The Problem With Receipts
#
# Your boss at the auto repair store # has given you three receipts that # he wants you to write a Python # program to process.

# The receipts are a mess: they
# have extra spaces in them at the # start and end.

# If the receipt has a "!" in it
# then it means that this customer # is a high volume customer.

# For each receipt:
# 1. Print out just the name
# 2. Set a Boolean variable if the # customer is a high volume customer
# 3. Print out the Boolean variable
# 4. Print out how much the
# customer spent
# 5. Print out what the customer
# purchased
#
# Student Name: Evagelos Petropoulos
#
receipt1 = "Bob Johnson  ! 127.52 Tires   "
receipt2 = "             Amy Johnson     35.18/ Oil Change  "
receipt3 = "      Tim Brown       ! 239.15 /  Alignment        "

#receipt1

#1.print out "Bob Johnson"
print(receipt1[:11])
#2. & 3. Set a Boolean variable if the # customer is a high volume customer and print out Boolean variable
receipt1_is_high_vol = receipt1.find('!')

if (receipt1_is_high_vol == -1): # if there is no '!' in the variable print False
    print(False)
else:                            # if there is a '!' in the variable print True
    print(True)
#4.Print out how much the customer spent
print(receipt1[15:21])
#5.Print out what the customer purchased
stripped_receipt1 = receipt1.rstrip()   #strips negative space
print(stripped_receipt1[-5:])           #negative index for ease of use

#receipt2
print('\n')     #new line for readability
#1.print out "Amy Johnson"
stripped_receipt2 = receipt2.strip()    #strips negative space
print(stripped_receipt2[:11])
#2. & 3. Set a Boolean variable if the # customer is a high volume customer and print out Boolean variable
receipt2_is_high_vol = receipt2.find('!')

if (receipt2_is_high_vol == -1): # if there is no '!' in the variable print False
    print(False)
else:                            # if there is a '!' in the variable print True
    print(True)

#4.Print out how much the customer spent
print(stripped_receipt2[16:21])
#5.Print out what the customer purchased
print(stripped_receipt2[-10:])           #negative index for ease of use

#receipt3
print('\n')     #new line for readability
#1.print out "Tim Brown"
stripped_receipt3 = receipt3.strip()    #strips negative space
print(stripped_receipt3[:9])
#2. & 3. Set a Boolean variable if the # customer is a high volume customer and print out Boolean variable
receipt3_is_high_vol = receipt3.find('!')

if (receipt3_is_high_vol == -1): # if there is no '!' in the variable print False
    print(False)
else:                            # if there is a '!' in the variable print True
    print(True)
#4.Print out how much the customer spent
print(stripped_receipt3[18:24])
#5.Print out what the customer purchased
print(stripped_receipt3[-9:])           #negative index for ease of use