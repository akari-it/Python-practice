x = 100

def test():  #defは定義しているだけで、関数を呼び出さないと中身は実行されない
    x = 50
    print(x)


print(x)
print(test()) #returnがない関数の戻り値はNone
              #print(test()) では、print() より先に test() の中身が実行される