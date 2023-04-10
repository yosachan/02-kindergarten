# age = 8
# height = 120

# age = input("年齢を入力してください")
# print(type(age))
# height = input("身長を入力してください")
# print(type(height))

# age = int(age)
# height = int(height)
# print(type(age))
# print(type(height))

# if (10 <= age) and (120 <= height):
#     print("野ってもいいよ。")
# else:
#     print("乗っちゃーダメだよ。")

age = input("年齢を入力してください")
age = int(age)

# if (age <= 10) or (80 <= age):
#     print("ダメぇ～")
# else:
#     print("いいよ")

if not( age < 10):
    print("いいよ")
else:
    print("ダメ")