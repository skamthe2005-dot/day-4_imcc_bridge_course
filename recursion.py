# def num(n):
#     if n==0:
#         return 0 
#     print(n)   
#     num(n-1)
# n=10
# num(n)

#recursion
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    

# n=5
# print(factorial(n))

#square of no
square=lambda n:n*n
print(square(5))

#addition of no
addition=lambda a,b : a+b
print(addition(3,5))

def fun(n):
    if n==0:
        return 
    fun(n-1)
    print(n)

fun(3)
    
