try:
	l=int(input())
	temp=l
	rev=0
	while(temp!=0):
		rem=temp%10
		rev=rev*10+rem
		temp=int(temp/10)
	if rev==l:
		print('palindrome')
	else :
		print('not palindrome')
except:
	print('invalid')
        
