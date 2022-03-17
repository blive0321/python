import time

taipeiTime = time.time()
print(taipeiTime)                                # 1647481856.0534453

print(time.localtime(taipeiTime))                # time.struct_time(tm_year=2022, tm_mon=3, tm_mday=17, tm_hour=9, tm_min=54, tm_sec=4, tm_wday=3, tm_yday=76, tm_isdst=0)

# time.asctime([t]) 把time tuple轉換成string
print(time.asctime(time.localtime(taipeiTime)))  # Thu Mar 17 09:54:50 2022

# time.strftime(format[,t]) format要填上格式化指令
print(time.strftime("%Y-%m-%d %H:%M:%S"))        # 2022-03-17 10:00:53