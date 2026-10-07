x=int(input("enter no:"))
sum=0
while x > 0:
    ld=x%10
    sum=sum+ld
    x=x//10
print(sum)

    