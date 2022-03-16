# list =  ['a','b','c']
# list is different than string in data type of python

##################### list() to create list #####################
# 1. string turn into list
print(list('basketball'))
# ['b', 'a', 's', 'k', 'e', 't', 'b', 'a', 'l', 'l']

# 2. tuple turn into list
sports = ('football','basketball')
print(list(sports))
# ['football', 'basketball']

# 3. 用string的方法split() 建立list
# split(分隔的依據, 分成幾個)
date = '2021/10/20'
print(date.split('/'))  # 因為第二個參數沒有輸入，所以分割全部。 
print(date.split('/',1))
# ['2021', '10', '20']      
# ['2021', '10/20']

aa = '1 2 3 4 5 6 7 8'.split()
print(aa)
# ['1', '2', '3', '4', '5', '6', '7', '8']


##################### basic functions #####################
# 1. len() 取得項目數量
print(len(aa)) # show 8

# 2. index() 找到項目的位置
print(sports.index('basketball')) # show 1

# 3. in , not in  will return Ture or False
print('basketball' in sports)
print('swimming' not in sports)

# 4. count() 計算項目出現的次數
print(sports.count('basketball')) # 1
print(sports.count('swimming'))   # 0


##################### 串列的提取、改變、增減、排序操作 #####################
# 1. 提取單一項目
student = ['brandon','liz','alex','claire']
print(student[0])
print(student[-1])

# 2. 提取子串列 使用slice[]
# [起點 : 終點 : 間隔]
print(student[0:2])
# ['brandon', 'liz']

# 3. 多重指定 (multiple assignment)
a1, a2, a3, a4 = student
print(a1) # brandon
print(a2) # liz

# 4. 改變串列內的項目
student[2] = 'vivian'
print(student)

# 除了上述一次改變一個項目外，也可以運用 slice[]，同時改變多個項目
red = ['flower', 'blood', 'hair', 'cake', 'bird', 'cloud']
red[1:4:2] = ['dog', 'tomato']
print(red)

# 5. 增加項目
# extend()
new_student = ['amber','linda']
student.extend(new_student)
print(student)

# insert(offset , '項目')
student.insert(0,'nana')
print(student)
# ['nana', 'brandon', 'liz', 'vivian', 'claire', 'amber', 'linda']

# append() 將項目加入到尾端
student.append('micky')
print(student)
# ['nana', 'brandon', 'liz', 'vivian', 'claire', 'amber', 'linda', 'micky']

# 6. 刪除項目
del student[0:-1:3]
print(student)
