# f=open("demo.txt","r")
# data=f.readlines()
# print(data)

# for names in data:
#     x=names[0]
#     f=open(f"{x}.txt","a")
#     f.write(names)

# f=open("demo.txt","r")
# data=f.readlines()
# list=[{i.strip() for i in data }]
# print(list)

# set=list[{1,1,1,1,}]
# print(type(set))
# print(set)

# list=["saurav","om","shivam","mahesh"]
# list.sort(key=len)
# print(list)

f=open("demo.txt","r")
data=f.readlines()
# list=[i.strip() for i in data]
for i in data:
    x=i[0]
    f=open(f"{x}.txt","a")
    f.write(i)

















