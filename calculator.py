print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.factorial")
print("6.exit")


while True:

    choice=int(input("enter your choice:"))

    if choice>6:
        print("enter valid input")

    elif choice==1:
        a=int(input("enter no:"))
        b=int(input("enter no:"))
        z=a+b
        print("sum =",z)
    elif choice==2:
        a=int(input("enter no:"))
        b=int(input("enter no:"))
        z=a-b
        print("substrtion =",z)
    elif choice==3:
        a=int(input("enter no:"))
        b=int(input("enter no:"))
        z=a*b
        print("multiplication =",z)
    elif choice==4:
        a=int(input("enter no:"))
        b=int(input("enter no:"))
        z=a/b
        print("division =",z)
    elif choice==5:
        a=int(input("enter no:"))
        fact=1
        for i in range(1,a+1):
            fact=fact*i
        print("fact =",fact)

    elif choice==6:
        print("thank you")
        break

