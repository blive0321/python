def caculator(CB):
    def run():
        result=0
        for n in range(51):
            result += n
        # print(result) # 不讓裝飾器print
        CB(result) # 把result傳給callback的Ans接收
    return run

@caculator
def showChinese(Ans):
    print(f"計算結果是: {Ans}")

@caculator # 重複利用裝飾器，只要寫@就可以加裝飾器，非常簡潔
def showEnglish(ANS):
    print(f"Result is: {ANS}")

showChinese()
showEnglish()