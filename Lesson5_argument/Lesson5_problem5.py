import random

number = random.randint(1,5)

def omikuji(number):
    if number == 1:
        print("大吉！")
    elif number == 2:
        print("大凶…")
    elif number == 3:
        print("小吉")
    else:
        print("中吉")


omikuji(1)
omikuji(2)
omikuji(4)

omikuji(number)
