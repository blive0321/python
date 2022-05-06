# Binary Search 二元搜尋演算法
# 使用此演算法有2個前提
# 1. 序列必須是"排序過"的序列
# 2. 序列中沒有重複的元素
# 概念:像是終極密碼一樣，taget為爆炸的號碼，每次猜數字都是對半猜，當沒猜到就縮小範圍，直到猜到為止

class Solution:
    # 箭號->為註解函數的return值類型為int
    def search(self, nums, target) -> int:
        # 定義offset值為left & right
        left, right = 0, len(nums) - 1

        while left <= right:
            # 對半猜, 抓對半的offset
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

nums = [5,10,15,20,25,30,35,40,45,50]
target = 40
Ans = Solution()
print("The target is at %d offset." %(Ans.search(nums , target)))
# The target is at 7 offset.