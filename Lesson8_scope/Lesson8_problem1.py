#スコープは簡単にいうと、その変数を使える範囲のこと。

price = 3000

def discount(price):
    price = price -500
    print (price)

discount(price)

print(price)