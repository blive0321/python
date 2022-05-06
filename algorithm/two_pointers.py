# two pointers雙指針演算法
# 給你一個遞增排序的整數陣列nums，return每個數字的平方並組成新的整數陣列，並且新的陣列也須依照遞增排序
# 譬如:nums = [-4,-1,0,3,10] 輸出:[0,1,9,16,100]，因平方後，整數變為[16,1,0,9,100]，排序後變為[0,1,9,16,100]

class Solution:
    def sortedSquares(self, nums:int) -> int:
        # n=5
        n = len(nums)
        # i=0, j=4, k=4
        i,j,k = 0, n-1, n-1
        # 宣告ans陣列=[-1, -1, -1, -1, -1]
        ans = [-1] * n

        while i <= j:
            # 整數陣列的最左邊
            lm = nums[i] ** 2
            # 整數陣列的最右邊
            rm = nums[j] ** 2
            
            if lm > rm:
                # 如果最左邊大於最右邊，就把最左邊的數，移到ans陣列最右邊
                ans[k] = lm
                i += 1
            else:
                # 如果最左邊沒有大於最右邊，就把最右邊的數，移到ans陣列最右邊
                ans[k] = rm
                j -= 1
            # 當最右邊的數放好後，ans的k指標-1
            k -= 1
        return ans

nums = [-4,-1,0,3,10]
Ans = Solution()
print("The new array is %s" %(Ans.sortedSquares(nums)))
# The new array is [0, 1, 9, 16, 100]