import sys
sys.setrecursionlimit(50000)
class Solution:
    def helper(self,A,low,high):
        if low>high:
            return None
        if(low==high):
            return A[low]
        mid=low+(high-low)//2
        if(mid%2==0):
            if(A[mid]==A[mid+1]):
                self.helper(A,mid+2,high)
            else:
                self.helper(A,low,mid)
        else:
            # if mid is odd the check for if mid is same in even postion(index)
            if(A[mid]==A[mid-1]):
                self.helper(A,mid+1,high)
            else:
                self.helper(A,low,mid-1)
        
    def solve(self,A):
        n=len(A)
        return self.helper(A,0,n-1)
        
if __name__ == "__main__":
    sol=Solution()
    mylist=[1,1,2,2,3,4,4]
    print(sol.solve(mylist))
