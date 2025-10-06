#print alternate Prime numbers in given range 
ll=int(input())
ul=int(input())
c=0
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            c+=1
            if c%2==0:
                print(n)