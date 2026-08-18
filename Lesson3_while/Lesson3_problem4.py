total = 0
i = 1

while i <= 100:
    total = total + i
    i = i + 1  # for文では i が自動的に次の数字になっていたけど、
               # while文では自分で i = i + 1 と書く必要がある
print(total)