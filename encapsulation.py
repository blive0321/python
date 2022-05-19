# Encapsulation 封裝，概念有點像是權限控制，希望某些屬性或方法封裝隱藏起來，不給類別外的人使用，可保護程式碼的商業邏輯避免被惡意使用者竊取
# 須使用"private attributes/methods私有屬性/方法"來實踐封裝

# Encapsulation is one of the four fundamental concepts in object-oriented programming including abstraction, encapsulation, inheritance, and polymorphism.

# 下面例子我們建立的Counter class，呼叫了increment() 2次，並把current變數設為-999，但你要如何避免current變數被Counter class的外面更改呢? 這時private attributes私人屬性就因此而誕生
class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0

counter = Counter()
counter.increment()
counter.increment()
counter.current = -999
print(counter.value())
# -999


# 一個underscore底線
# 私人屬性只能被class的method函式存取，換句話說，它們不能被class的外界存取
class Counter2:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0

counter = Counter2()
counter.increment()
counter.increment()
counter.current = -999 # 因變數加上single underscore後變成私人屬性，無法從外界更改為-999
print(counter.value())
# 2

# 兩個underscore底線
# Name Mangling名稱修飾，主要是為了避免外界對特定屬性的意外存取，或是不小心覆寫了父類別的的屬性、方法
class Counter3():
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0

counter = Counter3()
print(counter.__current) # 存取私人屬性會得到錯誤，因為有加上double score去封裝屬性
# AttributeError: 'Counter3' object has no attribute '__current'

counter.increment()
print(counter._Counter3__current) # 實際上python透過Name Mangling名稱修飾，把私有屬性重新命名，在前面加上底線類別，所以透過此名稱還是可以存取
# 1