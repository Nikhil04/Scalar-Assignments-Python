class stack:

    def __init__(self):
        self.__stack_arr=[]
        
    def push(self,object:any):
        self.__stack_arr.append(object)

    def pop(self):
        if self.isEmpty():
            print("Hey stack is empty")
            return 
        return (self.__stack_arr.pop())

    def top(self):
        if self.isEmpty():
            print("Hey stack is empty")
            return 
        return self.__stack_arr[len(self.__stack_arr)-1]

    def size(self):
        return len(self.__stack_arr)

    def isEmpty(self):
        return len(self.__stack_arr)==0
    
    def peekstack(self):
        return self.__stack_arr


if __name__ == "__main__":
    Mystack=stack()
    Mystack.push(2)
    Mystack.push(3)
    Mystack.push(6)

    while Mystack.isEmpty() is False:
        print(Mystack.pop())
    