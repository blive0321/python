# 輸入錯誤型別，程式沒有處理例外而丟到執行環境產生 "追蹤(Traceback)"並中斷程式
a = int(input('請輸入整數: '))
print(a)
# 請輸入整數: one
# Traceback (most recent call last):
#   File "try_except.py", line 1, in <module>
#     a = int(input('請輸入整數: '))
# ValueError: invalid literal for int() with base 10: 'one'



# 如果你想要處理例外，則可以使用try...except，下面例子，except可以指定多個物件，也可以有多個except，若使用者於輸入時輸入Ctrl+Z，在Windows環境下會引發EOFError，若輸入Ctrl+C，則會引發KeyboardInterrupt
try:
    b = int(input("請輸入整數: "))
    print(b)
except ValueError:
    print("請輸入阿拉伯數字")
except (EOFError, KeyboardInterrupt):
    print("使用者中斷程式")
# 請輸入整數: one
# 請輸入阿拉伯數字

# try還可以搭配finally，一但設置，無論有無引發物件，finally區塊一定會執行，這通常用來作為關閉若干資源的區塊，例如關閉檔案
file = open('if.py', 'r', encoding='UTF-8')
try:
    for line in file:
        print(line, end='')
except:
    print("讀取檔案發生錯誤")
finally:
    file.close()
