class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(0,len(nums)):
            if val != nums[i]:
                nums[k] = nums[i]
                k += 1
                

        return nums[:k]

Solution = Solution()
print(Solution.removeElement([0,1,2,2,3,0,4,2],2))                


