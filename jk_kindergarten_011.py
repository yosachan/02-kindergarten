a=100
if a==100:
    print("100点満点")
a=99
if a==100:
    print("１００点満点")
# a=input("数字を入力してください。")
# if a==100:
#     print("100点満点")
# else:
#     print("失敗") 
# str=input("文字列を入力してください。")
# if str.isdecimal():
#     print("数字です。")
# else:
#     print("数字でない")
moji=input("文字列を入力してください。")
if moji.isdecimal():
    print("数字です。")
elif moji.isalpha():
    print("文字列です。")
else:
    print("数字でも文字列でもない")







