number = int(input("ここに数字を入力してください"))
# inputはユーザーから入力してもらう
#　intは文字を数字に変換する

answer = 7

while number != answer:
    print("不正解！もう一度やり直してください")
    number =int(input("もう一度数字を入力してください"))
if number == answer:
    print("正解！")

#数字あてゲームができた！