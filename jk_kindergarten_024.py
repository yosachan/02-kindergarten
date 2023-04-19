dict_obj = {'dog':'犬', 'cat':'ねこ'}
print(len(dict_obj))
tuple_obj = (1, 2, 3)
print(len(tuple_obj))
list_obj = [1, 2, 3, 4]
print(len(list_obj))
str_obj = "12345"
print(len(str_obj))
dict1 = {'dog':'犬', 'cat':'ねこ'}
dict2 = {'dog':'犬', 'cat':'ねこ'}
print(dict1 == dict2)
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 5]
print(list1 == list2)
list_obj = ['note', 'book', 'pen']
print('book' in list_obj)
print('pencil' in list_obj)
tuple_obj = (1, 2, 4, 8, 16)
print(1 in tuple_obj)
print(7 in tuple_obj)
dict_obj = {'dog':'犬', 'cat':'ねこ', 'parrot':'オウム'}
print('dog' in dict_obj)
print('flog' in dict_obj)
str_obj = 'abracadabra'
print('abr' in str_obj)
print('www' in str_obj)
list_obj = ['apple', 'orange', 'banana']
for furut_name in list_obj:
    print(furut_name.upper())
tuple_obj = ('apple', 'orange', 'banana')
for furut_name in tuple_obj:
    print(furut_name.upper())
str_obj = 'hello'
for letter in str_obj:
    print(letter.upper())
dict_obj = {'dog':'犬', 'cat':'ねこ', 'parrot':'オウム'}  
for eng in dict_obj:
    jap = dict_obj[eng]
    print(eng, jap)  
    
    




