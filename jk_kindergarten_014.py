# text = ""

# while text != "finish":
#     text = input("文字列を入力してください。") 
#     print(text, "と入力されました。")
    
# print("終わり")

cnt = 1

while cnt <= 10:
    text = input("数字を入力してください")
    if text == "":
        continue
    if text == "999":
        print("中断")
        break
    number = int(text)
    print(cnt, "回目", number * number)
print("終わり")

# i = 0

# while i < 10:
#     i = i + 1
#     if (i % 2) == 1:
#         continue
#     print(i, "is even")
