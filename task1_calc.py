import math

print('Choose mode:')
print('Scientific Mode', 'Press 1', sep = '    -->    ')
print('Programer Mode ', 'Press 2', sep = '    -->    ')

mode = int(input("Mode: "))

if(mode == 1):
	print('************************** Scientific Mode **************************')
	print('Operation:    \n'\
	      ' 2^x  --> Enter 1\t', \
	      'sqrt --> Enter 2\t', \
	      'log10--> Enter 3\n', \
	      'ln   --> Enter 4\t', \
	      '1/x  --> Enter 5\t', \
	      '|x|  --> Enter 6\n', \
	      'e^x  --> Enter 7\t', \
	      'x!   --> Enter 8\t', \
	      '10^x --> Enter 9\n')
		  
	op = int(input("op: "))
	x = int(input('Number: '))
	match op:
		case 1:
			print('2^x = ', math.power(2, x))
		case 2:
			print('sqrt(x) = ', math.sqrt(x))
		case 3:
			print('log10(x) = ', math.log10(x))
		case 4:
			print('loge(x) = ', math.log(x))
		case 5:
			print('1/x = ', 1/x)
		case 6:
			print('|x| = ', math.fabs(x))
		case 7:
			print('e^x = ', math.power( (math.e) ^ x ))
		case 8:
			print('x! = ', math.factorial(x))
		case 9:
			print('10^x = ', math.power(10, x))
	
elif(mode == 2):
	print('************************** Programmer Mode **************************')
	print('Input:    '\
	      'Dec --> Enter 10',\
	      'Bin --> Enter 2',\
	      'Hex --> Enter 16', sep='        ')
	numSysIn = int(input("Numbering System: "))
	n = input('Number: ')
	print("Dec: ",int(n ,numSysIn))
	print("Bin: ",bin(int(n ,numSysIn)).replace('0b',''))
	print("Hex: ",hex(int(n ,numSysIn)).replace('0x',''))
	