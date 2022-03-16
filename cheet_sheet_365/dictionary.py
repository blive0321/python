##################### 這就是字典dict #####################
# {'Muffin':39, 'Scone':25, 'Biscuit':20}
# 'Muffin'    - 鍵key
# 39          - 值value
# 'Muffin':39 - 項目item
# 字典有2個特性 : 1.可變的資料型態  2.沒有順序性


##################### 建立字典 #####################
student = {"brandon":29, "liz": 29, "max":28, "nina":28}
project = {} #create empty dict, 而空集合是set(), 有些許不同

# 1. use zip() to create dictionary
student = ["brandon","liz","max","nina"]
age = [29,29,28,28]
print(dict(zip(student,age)))
# {'brandon': 29, 'liz': 29, 'max': 28, 'nina': 28}

# 2. use dict comprehensions(字典生成式) to create dictionary
# pattern : {代表鍵的變數 : 代表值的變數 for 可迭代物}
print({x: x**2 for x in range(1,4)})
# {1: 1, 2: 4, 3: 9}


##################### basic functions #####################
# 1. 取得字典內的元素
stock = {"台積電":2 , "大立光":1 , "長榮":10}
print(stock['長榮'])

# 2. get() 取得字典內的元素，若不元素不存在則使用預設值
# pattern : 字典.get(鍵, 備用的值)
print(stock.get('特斯拉',9))
# 9 只會回傳value，key不會回傳
print(stock.get("台積電",10))
# 2 原本的value不會更改，除非key不存在時才會回傳備用值10

# 3. setdefault() 與上述get()有點類似，但不同之處在於，如果指定的key&value不在字典裡面，會自動幫你加進字典
stock.setdefault("亞馬遜",7)
print(stock)
# {'台積電': 2, '大立光': 1, '長榮': 10, '亞馬遜': 7}

# 4. keys() 取得所有的鍵
print(stock.keys())
# dict_keys(['台積電', '大立光', '長榮', '亞馬遜']) 回傳前面的dict_keys代表它是dict_keys資料型態
print(list(stock.keys())) 
# ['台積電', '大立光', '長榮', '亞馬遜'] 用list()回傳串列

# 5. values()
print(list(stock.values()))
# [2, 1, 10, 7]

# 6. items()
print(list(stock.items()))
# [('台積電', 2), ('大立光', 1), ('長榮', 10), ('亞馬遜', 7)]

# 7. in成員運算子
print("台積電" in stock)
# True

# 8. not in成員運算子
print("台積電" not in stock)
# False

# 9. 改變dict內的value
stock["大立光"] = 6
print(stock)
# {'台積電': 2, '大立光': 6, '長榮': 10, '亞馬遜': 7}

# 10. 使用 [] 與 = 增加dict的項目
stock["臉書"] = 12
print(stock)
# {'台積電': 2, '大立光': 6, '長榮': 10, '亞馬遜': 7, '臉書': 12}

# 11. 使用update() 將另一個字典加到舊的字典
stock_back = {"蘋果":11 , "網飛":13}
stock.update(stock_back)
print(stock)
# {'台積電': 2, '大立光': 6, '長榮': 10, '亞馬遜': 7, '臉書': 12, '蘋果': 11, '網飛': 13}

# 12. del刪除項目item
del stock["台積電"]
del stock["大立光"]
del stock["長榮"]
print(stock)
# {'亞馬遜': 7, '臉書': 12, '蘋果': 11, '網飛': 13}

# 13. len()計算有幾個項目item
print(len(stock))
# 4

# 14. clear() 刪除所有項目item
stock.clear()
print(stock)
# {}

