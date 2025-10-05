#Prime numbers in given range
ll=int(input())
ul=int(input())
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)