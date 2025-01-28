# AHPA #4 - The UPC Code
#
# Student Name: Evagelos Petropoulos

"""
Part 1: 

Your assignment is to take a UPC code, divide it up into its four parts, then print them out in separate fields on a single line. 

Use this UPC code:
(020357122682)

Note: the program has to work for ANY UPC code in this format…

Part 2: 

Assume that this item costs $275.15. I would like to buy 12 of them. On a single line print out quantity to purchase, unit cost, and total cost (7 digits, 2 digits of precision, with commas separating thousands)
"""
#
#Part 1
UPCCode = "020357122682"
itemCost = 275.15
quantity = 12 #for part 2
total_cost = 12 * itemCost

one_digit_code = UPCCode[0] #slicing string to get digit/s
manufacturers_code = UPCCode[1:6]
product_code = UPCCode[6:11]
check_digit_code = UPCCode[11]

#prints the four code variables taken from UPCCode by slicing method out in separate fields on a single print line
print('{0}\n{1}\n{2}\n{3}'.format(one_digit_code,manufacturers_code,product_code,check_digit_code)) 

#Part 2
print('Quantity to purchase: {0} \nUnit Cost: ${1} \nTotal Cost: ${2:7,.2f}'.format(quantity,itemCost,total_cost))


