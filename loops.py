# print a table of odd no from 1 to 10

x=int(input("enter odd no :"))
for i in range(11):
    if x%2!=0:
        print(x,"*",i,"=" ,x*i)
    else:
        print("enter valid no")
        break

# create a heterogenous list of numbers and names split the list from highest number
# add the two no's at third position of the list and append in name in the list and split

list=[10,'saurav',90,'shivam',80,'ajay']
list.insert(3(8,9))
list.append("mahesh")
numbers=[x for x in list if isinstance(x,(int,float))]
# print(numbers)
highest_no=max(numbers)
# print(highest_no)
split_index=list.index(highest_no)
# print(split_index)
part1=list[:split_index]
part2=list[split_index:]
print(part1,part2)




# accept the name and check if it is palindrom

x=str(input("enter a string:"))
rev=x[::-1]
if x==rev:
    print("it is palindrom")
else:
    print("it is not")

# print the sum of digits

x=int(input("enter a no:"))
temp=x
sum=0

while temp>0:
    ld=temp//10
    sum+=ld
    temp=temp//10
print(sum)

# print this pattern
#  *
#  ##
#  ***
x=int(input("enter no:"))
for i in range(1,x+1):

    for j in range(i):
        if i%2!=0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()


# add the two no's at third position of the list and append in name in the list and split


        









