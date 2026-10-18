# f=open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()

f=open("sample.txt","a")
data=f.write("this is sample.txt file")
# data2=f.read()

# print(data[::-1])
f.close()
f2=open("sample.txt","r")
data2=f2.read()
print(type(data2))
print(data2[::-1])
f2.close()


