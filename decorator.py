# decorator 裝飾器本質上是一個函式，是用來輔助其它一般的函式
# 使用decorator會先執行裝飾器內部的程式碼，再執行callback(callback其實就是本來的函示)函式的程式碼

# ------------ 上半部 : 定義裝飾器的結構 ------------
# def 裝飾器名稱(定義callback函式名稱)
    # def 內部函式名稱():
        # callback函式()
    # return 內部函式名稱

# ------------ 下半部 : 使用裝飾器 ------------
# @裝飾器名稱
# def 函式名稱():
#     # 程式碼

# 函式名稱() #呼叫帶有裝飾器的函示


import time

def timer(func):
    def wrap(sleep_time):
        print("裝飾器的內部函式先執行")
        t_start = time.time()
        sleep_time += 1
        print("執行callback, 也就是外部函式dosomething")
        func(sleep_time) # callback function，其實就是本來的函示dosomething(sleep_time)這個函式
        t_end = time.time()
        t_count = t_end - t_start
        print("再回到內部函式")
        print('[花費時間]', t_count)

    return wrap

@timer
# 等於 foo = timer(dosomething)
def dosomething(sleep_time):
    print(f"do some thing, sleep {sleep_time} sec.")
    time.sleep(sleep_time)

dosomething(3) #呼叫帶有裝飾器的函示
_
# 裝飾器的內部函式先執行
# 執行callback,也就是外部函式
# do some thing, sleep 4 sec.
# 再回到內部函式
# [花費時間] 4.004133462905884
