# -------------- 物件導向 Object Oriented Programming --------------
# 類別 (Class)
# 建構式 (Constructor)
# 方法 (Method)
# 屬性 (Attribute)
# 物件 (Object)
# CCMAO類建方屬物
# __雙底線的英文唸法:dunder


# class 類別
class Person: 

    # Attribute 屬性
    group = "ABC Company Team 100"
    
    # def __init__(self, name, age): Constructor 建構式
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    
    # def function(self): Method 方法
    def say(self):
        print(f'Hi, my name is {self.name}, I am {self.age} years old.')


# mike = Persio() Object 物件
mike = Person('Mike', 20)
mike.say()
print(mike.group)

john = Person('John', 21)
john.say()
print(john.group)


# -------------- inherit 繼承 --------------
class Father():
    def __init__(self):
        self.house = 2

# Son物件繼承Father物件
class Son(Father): 
    def __init__(self, cars):
        #用super()來取得Father.__init__()的方法，這樣做法的好處，如果將來Father的定義改了，使用super()可確保Son從Father繼承而來的屬性與方法可以適時地跟著改變
        super().__init__()
        self.cars = cars

    def estate(self):
        print("==== Estate ====")
        print("house : ", self.house)
        print("cars : ", self.cars)


if __name__ == "__main__":
    brandon = Son(5)
    brandon.estate()
