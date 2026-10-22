# list=[]
# f=open('demo.txt',"r")
# data=f.readlines()
# for i in range(len(data)):
#     list.append(data[i])
# print(list)
# list=[]
# f=open('demo.txt',"r")
# data=f.readlines()
# for i in range(len(data)):
#     if len(data)>3:
#         list.append(data[i])
# list2=sorted(list)
# print(list2)
# for j in range(len(list2)):
#     print(type(list2[j]))
#     for k in range(len(list2[j])):
#         if list2[k]=='a':
#             print(list2[j])



# f2=open('sample.txt','w')
# for j in range(len(list)):
#     data2=f2.write(list[j])
# print(data2)



# count=0
# f=open('demo.txt',"r")
# data=f.readlines()
# for i in range(len(data)):
#     if data[i].startswith('a' or 'i' or 'e' or 'o' or 'u'):
#         count+=1
# print(count)

# dict={}
# f=open('demo.txt',"r")
# count=1
# data=f.readlines()
# for i in range(len(data)):
#     if data[i] in dict:
#         dict[data[i]]+=1
#     else:
#         dict[data[i]]=count
# print(dict)

names=[]
f=open('demo.txt',"r")
data=f.readlines()
for i in range(len(data)):
    x=data[i].strip()
    names.append(x)
names2=[]
for j in range(len(names)):
    if names[j] not in names2:
        names2.append(names[j])
        
names2.sort()
print(names2)




