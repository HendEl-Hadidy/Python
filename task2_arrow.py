n = int(input("Enter a number: "))
for i in range(n-1):
	for j in range(3*n):
		print(' ',end='')
	for j in range(i+1):
		print('*',end='')
	print()

for j in range(2*n):
		print(' ',end='')
for i in range(2*n):
	print('*',end='')
print()

for i in range(n-1):
	for j in range(3*n):
		print(' ',end='')
	for j in range(i, n-1):
		print('*',end='')
	print()