for i in range(1,21):
    amari = i % 2
    if amari == 0:
    # = ではなく ==  
    # =は代入、==は比較なのでif文では　==を使う 
       print(i)
       #ifとprintを同列にしてはいけないのは、
       # ifは条件で条件と処理は常にセットで行わないと意味がないから。