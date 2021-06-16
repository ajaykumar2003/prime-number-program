n=int(input("enter the value of n:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        print(i)
if c==2:
    print(n,"prime number")
else:
    print(n,"not a prime number")
