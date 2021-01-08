print("Welcome to do this Simple")

user_name=input("Enter Your Name: ")

listdata = 'anything'

datainlist = list()

def showMenu():
	print("Menu:")
	print("1. Add an item:")
	print("2. Mark as Done:")
	print("3. View Items:")
	print("4. Exit:")


while listdata != '4':

	showMenu()
	listdata = input("Enter Your Choice: ")

	if listdata == '1':
		item = input("What you would like to do ? ")
		datainlist.append(item)
		print("Added Item:", item)

	elif listdata == '2':
		item = input("What is to be marked as Done ")
		
		if item in datainlist:
			datainlist.remove(item)
			print("Item Removed:", item)
		else:
		    print("This item does not exist in the to-do list ")

	elif listdata == '3':
		print("List of TO-DO Items: ")
		for items in datainlist:
			print(items)
	    
	elif listdata == '4':
	    print("Thank you for using the tool SAN {}. Have a Great day!".format(user_name))