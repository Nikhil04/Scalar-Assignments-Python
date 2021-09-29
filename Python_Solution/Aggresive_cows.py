import sys
sys.setrecursionlimit(50000)
class solution:
    def check(self,arr,B,n,mid):
        count=1
        lastpos=arr[0]
        for i in range(1,n):
            if(arr[i]-lastpos>=mid):
                lastpos=arr[i]
                count+=1
            if(count==B):
                return True
        return False

    def solve(self,A,B):
        arr=sorted(A)
        n=len(A)
        start=0
        end=arr[n-1]-arr[0]
        ans=0
        while(start<=end):
            mid=start+(end-start)//2
            if(self.check(arr,B,n,mid)):
                ans=mid
                start=mid+1
            else:
                end=mid-1
        return ans

if __name__ =="__main__":
    mysol=solution()
    A=[1,2,3,4,5,6]
    B=3
    print(mysol.solve(A,B))