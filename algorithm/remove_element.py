# Hare & Tortoise 快慢指針演算法
# 給你一個陣列nums和一個值val，移除所有值等於val的元素，並return移除後新的陣列長度
# 譬如:nums = [0,1,2,2,3,0,4,2], val = 2, 移除2之後return陣列新的長度5，且前5個元素變為 [0,1,3,0,4]

class Solution:

    # class method跟class variable一樣，都是用在class本身，而不是用在物件上
    @classmethod
    def removeElement(cls, nums, val) -> int:
        # 設定快指針和慢指針的offset
        fast = slow = 0
        
        # 當快指針offset比陣列的長度還少時，就繼續算
        while fast < len(nums):

            # 當快指針不等於val值的時候，慢指針也等於快指針
            # 當快指針一等於val值的時候，快指針offset+1
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        # 當快指針offset等於陣列長度len(nums)時，等於遍歷完所有元素了，就return慢指針的offset
        return slow

nums = [1,2,3,3,5,3,7,9]
val = 3
Ans = Solution()
print("After remove the val, the lens of the list is %d" %(Ans.removeElement(nums , val)))
# After remove the val, the lens of the list is 5
