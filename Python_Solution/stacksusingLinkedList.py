from itertools import count
from requests import head
from nodeclass import node as Node

class stack_ll:

    def __init__(self):
        self.__head=None
        self.__count=0
    
    def push(self,element:any):
        newelement=Node(element)
        newelement.next=self.__head
        self.__head=newelement
        self.__count+=1

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return 
        data=self.__head.data
        self.__head=self.__head.next
        self.__count-=1
        return data

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return 
        top=self.__head.data
        return top

    def isEmpty(self):
        return  self.size()==0

    def size(self):
        return  self.__count

if __name__ == "__main__":
    Mystack=stack_ll()
    Mystack.push(2)
    Mystack.push(3)
    Mystack.push(6)
    print(Mystack.isEmpty())
    print(Mystack.top())
    Mystack.pop()
    while Mystack.isEmpty() is False:
        print(Mystack.pop())
    print(Mystack.isEmpty())