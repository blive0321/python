# -------------- 物件導向繼承 Object Oriented Inherit Programming --------------
# 以下內容為，宣告類別，並建立多個物件，再用for迴圈call多個物件的屬性、方法

from collections import OrderedDict

# 宣告class Prosche，並設定屬性Attributes和方法Method
class Porsche:
    def __init__(self,bmcip,uutip,brand):
        self.bmc = bmcip
        self.uut = uutip
        self.proj = brand

    def go(self):
        print("Hello World, this is 'go' function.")

# OrderedDict()的特性，就是對key做排序，排序依據是key先後被插入的順序，如果更新某個value，並不會影響它在OrderedDict()的排序
GOAL = OrderedDict()

# File I/O去逐行讀./IPTable
File_IPTable=open("./IPTable","r")
for ip in File_IPTable.readlines():
    ip = ip.strip('\n')
    bmc = 'b' + ip
    uut = 'r' + ip
    # for迴圈會逐一建立物件GOAL[ip1], GOAL[ip2]，並都會繼承Porsche類別
    GOAL[ip] = Porsche(bmc,uut,'Porsche')
File_IPTable.close()

print(" ------------------------------------ ")

print(type(GOAL[ip]))                                           # <class '__main__.GOAL'>
print(GOAL[ip])                                                 # <__main__.GOAL object at 0x7f56d2a1da58>
GOAL[ip].go()                                                   # Hello World, this is 'go' function.
print(GOAL[ip].bmc)                                             # b022402.slot1  不用for迴圈只會印出最後一個
print(GOAL[ip].uut)                                             # r022402.slot1
print(GOAL[ip].proj)                                            # GOAL

for DUT in GOAL:
    print(" =============================================== ")
    print("DUT  = "+DUT)                                         
    print("GOAL = " + GOAL[DUT].bmc + ' & ' + GOAL[DUT].uut )   

#  ===============================================
# DUT  = 033103.slot2
# GOAL = b033103.slot2 & r033103.slot2
#  ===============================================
# DUT  = 022402.slot1
# GOAL = b022402.slot1 & r022402.slot1

