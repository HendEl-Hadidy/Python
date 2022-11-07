price = {
	"Apple" : 30,
	"Banana": 15,
	"Cherry": 20
}

quantaty = {
	"Apple" : 78,
	"Banana" : 84,
	"Cherry" : 145
}

order = {}

print("************************************* Welcome to iTi Shop :) ***************************************")
print('Mode:\n',\
	  'Customer --> Enter 1',
	  'Owner--> Enter 2',
	  'Exit --> Enter 0', sep = '    ')
mode = int(input("Mode: "))
if(mode == 1):
	print('Show products  --> Enter 1',\
		  'Buy products   --> Enter 2',\
		  'Print the bill --> Enter 3',\
		  'Back           --> Enter 0',sep='\n')
		  
	choice = int(input('Ans: '))
	if(choice == 1):
	for x, y in price.items():
		print(x, ':  ', y, ' L.E/Kg')

	elif(choice == 2):
	while(True):
		item = input('item: ')
		if (item == 'stop'):
			break
		quan = int(input('quantity: '))
		order[item] = quan
	total = 0
	print('item\t', 'price\t', 'quantity\t', 'total')
	for x, y in order.items():
		print(x, '\t', price[x], '\t', y, '\t\t', y*price[x])
		total += y*price[x]
	print("\ntotal = ", total, " L.E")
	'''	
	elif(choice == 3):
	print('item\t', 'price\t', 'quantity\t', 'total')
	for x, y in order.items():
		print(x, '\t', price[x], '\t', y, '\t', y*price[x])
	
	# elif(Choice == 0):
	'''

elif(mode == 2):
	print('Show products  --> Enter 1',\
		  'Add products   --> Enter 2',\
		  'Modify prices  --> Enter 3',\
		  'Back           --> Enter 0',sep='\n')
		  
	choice = int(input('Ans: '))
	if(choice == 1):
	for x, y in price.items():
		print(x, ':  ', y, ' L.E/Kg')

	elif(choice == 2):
		while(True):
			item = input('item: ')
			if (item == 'stop'):
				break
			pricee = int(input('quantity: '))
			price[item] = pricee
        for x, y in price.items():
		print(x, ':  ', y, ' L.E/Kg')
	
	elif(choice == 3):
		while(True):
			item = input('item: ')
			if (item == 'stop'):
				break
			pricee = int(input('quantity: '))
			price[item] = pricee
        for x, y in price.items():
		print(x, ':  ', y, ' L.E/Kg')

elif(mode == 0):
	print("Thank you")
else:
	print("Invalid Entery!")