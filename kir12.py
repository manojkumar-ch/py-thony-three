b=int(input('Enter the number to check: \n'))
rank=0
for i in range (2,b):
	if(b%i==0):
		rank = rank+1
if(rank==0):
	print('Yes, It is a prime number')
else:
	print('No, It is not a prime number')
