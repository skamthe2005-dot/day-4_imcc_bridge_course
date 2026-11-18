# from practice import stack


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


    def rev_stack(self,prevstack):
        s2=stack()
        while prevstack.top!=None:
            x=prevstack.pop()
            s2.push(node(x))
        s2.print()

        
    def print(self):
        temp=self.top
        while temp:
            print(temp.data)
            temp=temp.next
        

class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def isempty(self):
        return self.front==None

    def enqueue(self,value):
        newnode=node(value)
        if self.isempty():
            self.front=newnode
            self.rear=newnode
            return 
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        temp=self.front
        self.front=self.front.next
        return temp.data
    
    def reverse_q(self,prevq):
        s=stack()
        temp=self.front
        while self.front!=self.rear:
            x=prevq.dequeue()
            s.push(node(x))
        s.print()

            
    


    def printx(self):
        print(self.front.data)
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next
        


q=queue()

q.enqueue(10)
q.enqueue(20)
q.reverse_q(q)
# q.printx()

        