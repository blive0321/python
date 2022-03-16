# string = "abc"  single quote or double quote are the same

# backslash \t=tab, \n=enter
print('That\'s my job!')

##################### str() to create string #####################
str(123)
print(type(str(123)))

##################### basic functions #####################
# 1. len() 取得長度
word = "Hello world"
print(len(word))

# 2. r'' 顯示原始字串
word = r"That\'s my job!" #double quote has the same effect
print(word)

# 3. 取得子字串
print(word[0]) # T
print(word[0:7]) # That\'s

# 3. string相加使用
line1 = 'Do you like python?'
line2 = 'Yes, I love it.'
print(line1 +' '+ line2)

# 4. 字串插入變數
# % 在字串最後面%()內加入變數
product = "apple"
price = 55
sentence = "the %s is %d dollars" %(product, price)
print(sentence)

# f-strings 將變數直接加入{}裡
f_sentence = f"the {product} is {price} dollars"
print(f_sentence)

##################### 字串的修改 #####################
# 1. strip() 從兩側移除字元
word = "    Smart    "
print(word.strip())   #兩側
print(word.rstrip())  #右側
print(word.lstrip())  #左側
# Smart

# 2. split() 拆出多個字串
print("You work very hard".split()) #以空白字元來切割，並return list串列
# ['You', 'work', 'very', 'hard']

# 3. join() 此方法需要string + list這兩個data，利用string當膠水，把list黏起來，並return list串列
gift_list = ['PS5','XBOX360','SWITCH']
print("I want "+', '.join(gift_list))
# I want PS5, XBOX360, SWITCH

# 4. replace() (要被替換的值, 替換成這個值)
lesson = "My new goal : Python."
print(lesson.replace('Python','Speaking english'))

# 5. index() 或 find() 查offset值
fruits = "Apple, Guava, Kiwi"
print(fruits.index('Guava'))  # 回傳值的是字串首個字母的位置
# 7
