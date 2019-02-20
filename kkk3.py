try:
	k=int(input())
	temp=k
	rev=0
	while(temp!=0):
		rem=temp%10
		rev=rev*10+rem
		temp=int(temp/10)
	if rev==k:
		print('palindrome')
	else :
		print('not palindrome')
except:
	print('invalid')
