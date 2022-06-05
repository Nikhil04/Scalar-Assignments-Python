class balanced_paranthesis:

    s=[]

    def __init__(self):
        pass
        
    def check_balanced(self,string):
        for elem in string:
            if elem in "({[":
                self.s.append(elem)
            elif elem==")":
                if(len(self.s)==0 or self.s[-1]!="("):  #len(self.s)==0  is same as (not self.s)
                    return False
                self.s.pop()
            elif elem=="}":
                if(not self.s or self.s[-1]!="{"):
                    return False
                self.s.pop()
            elif elem=="]":
                if(not self.s or self.s[-1]!="["):
                    return False
                self.s.pop()
        if(not self.s):
            return True
        return False
            

if __name__ == "__main__":
    myString="[{(a+b)}]"
    solution=balanced_paranthesis()
    print(solution.check_balanced(myString))