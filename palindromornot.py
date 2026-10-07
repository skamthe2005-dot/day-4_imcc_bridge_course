x=int(input("enter no:"))
rev=1
num=x
while num>0:
    ld=num%10
    rev=ld*10
    num=num//10
print(rev)    