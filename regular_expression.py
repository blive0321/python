import re


# ================  re.match('字串',變數) ================
TEST_1 = input("Enter TEST_1: ")
if re.match('Jordan',TEST_1):
    print("You do enter Jordan")
else:
    print("You don\'t enter Jordan ")

# ================  re.compile('正規表達')  +  fullmatch(物件 , 字串變數) ================
# 先建立tall 和 kg的正規表達物件
re_tall = re.compile('[0-9]+cm')
re_kg = re.compile('[0-9]+kg')
TALL = input("Enter your tall(+cm): ")
WEIGHT = input("Enter your weight(+kg): ")
if re.fullmatch(re_tall , TALL):
    print(f"You are {TALL} height.")
if re.fullmatch(re_kg , WEIGHT):
    print(f"and you are {WEIGHT} weight.")
# Enter your tall(+cm): 170cm
# Enter your weight(+kg): 70kg
# You are 170cm height.
# and you are 70kg weight.

# match開頭符合 , fullmatch完全符合

