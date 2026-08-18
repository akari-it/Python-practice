import random

def omikuji():
    number =random.randint(1,10)

    if number == 10:
        return "大吉！"
    elif number >= 8:
        return "中吉"
    elif number >= 4:
        return "小吉"
    elif number >= 2:
        return "凶"
    else:
        return "大凶…"

result =omikuji()

print ("今日の運勢は" + result)