# 滑動窗口演算法(也是雙指針的一種)
# 給妳有n個正整數的陣列，和一個正整數s，找出該陣列中的元素組合有滿足>=s的，且長度最小的那一個子陣列，並return子陣列的長度，如果不符合條件，則return 0
# s = 7 , nums = [2,3,1,2,4,3]  輸出:2，因為子陣列[4,3]是符合>=s且長度最小的陣列

from re import X


class Solution:
    def minSubArrayLen(self, s: int, nums: int) -> int:
        # result為最終結果的變數
        result = float("inf")
        # Sum為子陣列的數值和
        Sum = 0
        # index為子陣列的長度
        index = 0

        # i = 0, 1, 2, 3, 4, 5
        for i in range(len(nums)):
            # Sum = Sum + nums[i]
            Sum += nums[i]
            # 一旦子陣列的和 >= s，就更新result
            while Sum >= s:
                # i-index+1是算窗口裡的元素數量，i是窗口最右邊的offset，index是窗口最左邊的offset，減完要再+1回來
                result = min(result, i-index+1)
                # Sum窗口減去最左邊的值
                Sum -= nums[index]
                # 從0遞增子陣列的index
                index += 1
        return 0 if result == float("inf") else result

nums=[2,3,1,2,4,3]
Ans = Solution()
print(Ans.minSubArrayLen(7 , nums))

# i  sum  sum>=7  i-index+1  result  sum-num[index]  index
# 0  2    no
# 1  5    no
# 2  6    no
# 3  8    yes     3-0+1=4    4        8-2=6          0+1=1
# 4  10   yes     4-1+1=4    4        10-3=7         1+1=2
#    7    yes     4-2+1=3    3        7-1=6          2+1=3
# 5  9    yes     5-3+1=3    3        9-2=7          3+1=4