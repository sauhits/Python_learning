# ランダムに0~100の数値を作成
import random

rand_int = random.randint(0, 100)

if rand_int % 2 == 0:
    print("偶数です")
else:
    print("偶数ではありません")
