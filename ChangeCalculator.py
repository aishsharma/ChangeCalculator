"""
Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and pennies are needed to make up the amount needed. 
For example, if he inputs 1.47, the program will tell that he needs $1 and 1 quarters, 2 dimes, 0 nickels, and 2 pennies.
"""
import string

def main():
	givenAmount = input("Enter amount given by customer: ")
	bill = input("Enter customer's bill: ")
	
	try:
		change = float(givenAmount) - float(bill)
	except ValueError:
		print("Amount should be a valid integer or decimal value. Eg: 25 or 5.67")
		main()
	
	if change < 0:
		print("The customer needs to give you more money")
		main()
	elif change == 0:
		print("No change to be returned.")
	else:
		print("Change = ", change)
		amountParts = str(change).split(".")
		
		bigPart = int(amountParts[0])
		smallPart = int(amountParts[1])
		
		print("You need to return: $", bigPart, "and")
		
		#Getting number of coins
		smallPart = getQuarters(smallPart)
		smallPart = getDimes(smallPart)
		smallPart = getNickels(smallPart)
		getPennies(smallPart)
		
		
def getQuarters(smallPart):
	numberOfQuarters = 0
	if smallPart >= 25:
		numberOfQuarters = int(smallPart / 25)
		smallPart = smallPart % 25
	
	print(numberOfQuarters," quarters.")
	return smallPart

def getDimes(smallPart):
	numberOfDimes = 0
	if smallPart >= 10:
		numberOfDimes = int(smallPart / 10)
		smallPart = smallPart % 10
	
	print(numberOfDimes," dimes.")
	return smallPart
	
def getNickels(smallPart):
	numberOfNickels = 0
	if smallPart >= 5:
		numberOfNickels = int(smallPart / 5)
		smallPart = smallPart % 5
	
	print(numberOfNickels," nickels.")
	return smallPart
	
def getPennies(smallPart):
	numberOfPennies = 0
	if smallPart >= 1:
		numberOfPennies = smallPart
	
	print(numberOfPennies," pennies.")