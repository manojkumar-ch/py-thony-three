c,d=map(int,input().split())
for i in range(c+1,d):
  if(i%2==0):
    if (i!=d-1 and i!=d-2):
      print(i,end=' ')
    else:
      print(i,end='')
