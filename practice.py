class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    def push(self,node):
        if self.top==None:
            self.top=node
            return 
        else:
            node.next=self.top
            self.top=node

    def pop(self):
        if self.top==None:
            print("stack is empty")
            return
        else:
            topcopy=self.top
            self.top=self.top.next
            topcopy.next=None
        return topcopy.data

    def reverse_string(self,value):
        for i in value:
            self.push(node(i))
        return
            # if self.top==None:
            #     self.top=i
            #     return
            # for j in value:
            #     j.next=self.top
            #     self.top=j
            # while self.top !=None:
            #     print(self.pop())

    def rev_stack(self,prevstack):
        s2=stack()
        while prevstack.top!=None:
            x=prevstack.pop()
            s2.push(node(x))
        s2.print()




    # def reverse_stack():
    #     while s:
    #         x=s.pop()
    #         if s2.top==None:
    #             s2.top=node(x)
    #             return
    #         else:
    #             node(x).next=s2.top
    #             s2.top=node(x) 
    #     return s2
        
    def print(self):
        temp=self.top
        while temp:
            print(temp.data)
            temp=temp.next




s=stack()
# s2=stack()
# s.push(node(10))
# s.push(node(20))
# s.push(node(30))
# s.push(node(40))
# s.reverse_string("saurav")
# print(s.pop())
# s.print()
# s.rev_stack(s)

# def reverse_stack():
#     while s:
#         x=s.pop()
#         if s2.top==None:
#             s2.top.next=node(x)
#             s2.top=node(x)
#         else:
#             node(x).next=s2.top
#             s2.top=node(x)
        
#     return s2
    

# print(reverse_stack())
# print(reverse_stack())






        








     
