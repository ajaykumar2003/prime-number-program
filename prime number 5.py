n=int(input("enter the value of a"))
import math
s=int(math.sqrt(n))
c=0
for i in range(1,s+1):
    if n%i==0:
        c+=1
if c>1:
    print(n,"not a prime number")
else:
    print(n,"is a prime number")
