# dict_obj = {'dog':'犬'}
# print(dict_obj['dog'])
# dict_obj['dog'] = 'わんこ'
# print(dict_obj['dog'])

# dict_obj = {'dog':'犬', 'cat':'ねこ'}
# print(dict_obj)
# del dict_obj['dog']
# print(dict_obj)

# dict_obj = {'dog':'犬', 'cat':'ねこ'}
# print(len(dict_obj))
# dict_obj['pengin'] = 'ペンギン'
# print(dict_obj)
# print(len(dict_obj))
# del dict_obj['cat']
# print(dict_obj)
# print(len(dict_obj))

# dict_obj = {'dog':'犬', 'cat':'ねこ', 'pengin':'ペンギン'}
# print('dog' in dict_obj)
# print('apple' in dict_obj)

eng_obj = {'apple':'りんご', 'orange':'みかん', 'peach':'もも'}
input_word = input('文字列をにゅりょくしてください。')
if input_word in eng_obj:
    print(eng_obj[input_word])
else:
    print('NG')



