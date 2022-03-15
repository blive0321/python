# Python 的 built-in function 內建函數可以隨時隨地的被呼叫，不需要import module

# 1. abs() 返回數字的絕對值
from hashlib import new


print("abs(-25) =",abs(-25))       # abs(-25) = 25
print("abs(100.12) =",abs(100.12)) # abs(100.12) = 100.12

# 2. all(iterable) 判斷傳入的可迭代參數裡的元素，是否都回True，若元素是0、空、None、False則為False
print(all([1,2,3,4]))              # True
print(all([1,2,3,0]))              # False
print(all([]))                     # 注意,空串列為True
print(all(()))                     # 注意,空tuple為True

# 3. divmod(x,y) 求商數和餘數
print(divmod(6,2))                 # (3, 0)
print(divmod(7,2))                 # (3, 1)

# 4. enumerate(sequence, [start=0]) 將一個可以遍歷的sequence(ex:list, tuple, string)，組合為一個索引序列，並印出來 []代表可選可不選，設定索引開始的數字
seasons = ["spring","summer","fall","winter"]
for id, weather in enumerate(seasons,start=7):
    print(id,weather)
# 7 spring
# 8 summer
# 9 fall
# 10 winter

# 5. eval(expression[, globals[, locals]]) 用來執行字串表達式，並return表達式的值
x = 7
print(eval("3 * x"))                # 21

# 6. exec(object[, globals[, locals]]) 用來執行python的字串表達式，相對eval可以執行更複雜的python code
exec('print("Hello World")')        # Hello World

# 7. filter(function, iterable) 用來過濾可迭代的iterable序列(ex:list)，過濾掉符合或不符合條件的元素，序列的每個元素傳給函數作為判斷，然後retrun True或False，返回True的元素存到新的列表中
def is_odd(n):
    return n % 2 == 1

newlist = filter(is_odd, [1,2,3,4,5,6,7,8,9,10])
print(list(newlist))                 # [1, 3, 5, 7, 9] 找出奇數

# 8. hash(object) 計算hash雜湊值，可用來校驗檔案傳輸前和傳輸後的hash值是否一樣，若hash值不一樣則代表檔案內容有更動或有掉包
file="ac-cycle"
print(hash(file))                    # 8148203886928610989

# 9. hex(x) 將整數轉成string格式的十六進制
print(hex(255))                      # 0xff
print(type(hex(255)))                # <class 'str'>

# 10. input([prompt]) 接收標準輸入，並return string格式
a = input("Please type here :")      # Hey, man
print(a)                             # Hey, man

# 11. int(x, base=10) 將字串或數字，轉換為十進制的數字
print(int(2))                        # 2
print(int("16",base=10))             # 16

# 12. map(function, iterable) 將可迭代iterable序列的每個元素，傳至function，並return新的列表
def square(x):
    return x ** 2

newlist = map(square, [1,2,3,4,5])
print(list(newlist))                 # [1, 4, 9, 16, 25]