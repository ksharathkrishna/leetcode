class Solution:
    # Refer https://chatgpt.com/c/de9c6f0b-62ec-49c3-a343-1dede3e23928
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        prefixCount=[0]* (n+1)
        for i in range(n):
            if nums[i]%2: prefixCount[i+1]=prefixCount[i]+1
            else: prefixCount[i+1]=prefixCount[i]
        m={0:1}
        for i in range(1,n+1):
            t=prefixCount[i]-k
            # m[t] represents no of vaild sub arrays wit h k odd number till i index
            if t in m:ans+=m[t]
            m[prefixCount[i]]=m.get(prefixCount[i],0)+1
        return ans