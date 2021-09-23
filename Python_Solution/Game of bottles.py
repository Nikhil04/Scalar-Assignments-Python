class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mydict={}
        for ele in A:
            if ele in mydict:
                mydict[ele]+=1
            else:
                mydict[ele]=1
        maxfreq=0
        mostbottles=0
        for k,v in mydict.items():
            if(v>maxfreq):
                maxfreq=v
                mostbottles=k
        return maxfreq,mostbottles

if __name__ == "__main__":
    cat=Solution()
    arr=[1, 2, 3]
    print(cat.solve(arr))
