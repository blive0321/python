# 物件導向 Object Oriented Programming
# 類別 (Class)
# 物件 (Object)
# 屬性 (Attribute)
# 建構式 (Constructor)
# 方法 (Method)


##################### basic #####################
class Person:

    group = "ABC Company Team 100"
    
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    
    def say(self):
        print(f'Hi, my name is {self.name}, I am {self.age} years old.')


mike = Person('Mike', 20)
mike.say()
print(mike.group)

john = Person('John', 21)
john.say()
print(john.group)


##################### inherit #####################
class Father():
    def __init__(self):
        self.house = 2

class Son(Father): #inherit Father class
    def __init__(self, cars):
        super().__init__()
        self.cars = cars

    def estate(self):
        print("==== Estate ====")
        print("house : ", self.house)
        print("cars : ", self.cars)


if __name__ == "__main__":
    brandon = Son(5)
    brandon.estate()
