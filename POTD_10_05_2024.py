#User function Template for python3

class Solution:
    def find_all_comb(self,trgt_sum,dummy_list,complete_list,iteration,given_array):
        if(trgt_sum==0):
            complete_list.append(dummy_list.copy())
            return
        for i in range(iteration,len(given_array)):
            if i>iteration and given_array[i]==given_array[i-1]:
                continue
            if given_array[i]>trgt_sum:
                break
            dummy_list.append(given_array[i])
            trgt_sum-=given_array[i]
            self.find_all_comb(trgt_sum,dummy_list,complete_list,i+1,given_array)
            dummy_list.pop()
            trgt_sum+=given_array[i]
    
    def CombinationSum2(self, arr, n, k):
        dummy_list=[]
        comp_list=[]
        arr.sort()
        self.find_all_comb(k,dummy_list,comp_list,0,arr)
        return comp_list
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends
