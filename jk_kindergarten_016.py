# momo = ''
# mikan = ''

# momo = input('桃の個数を入力してください。')
# mikan = input('みかんの個数を入力してください。')

# if momo == '':
#     num_momo = 0
# else:
#     num_momo = int(momo)
    
# if mikan == '':
#     num_mikan = 0
# else:
#     num_mikan = int(mikan)

# total_momo = num_momo * 100
# total_mikan = num_mikan * 40

# total = total_momo + total_mikan

# print('合計は', total, '円です。')

# def fruit_price(num_momo, num_mikan):
#     total_momo = num_momo * 100
#     total_mikan = num_mikan * 40
#     total = total_momo + total_mikan
#     return total

# goukei = fruit_price(10, 40)
# print(goukei)

global_value = 200
def test_global(arg):
    return arg * global_value
print(test_global(10))


def func1(name):
    print('こんにちは、', name, 'これはfunc1です。')
def func2():
    func1('func2')
func2()


import time

def print_time():
    now = time.asctime()
    print('今は、', now)
print_time()


def func(arg1, arg2, arg3):
    print('arg1は：', arg1, 'arg2は：', arg2, 'arg3は：', arg3)
func('引数１', '引数２', '引数３')
func(arg1='引数１', arg2='引数２', arg3='引数３')


def func1(arg=999):
    print(arg)
func1(12345)
func1()


def fruit_price(num_momo, num_mikan, name="上"):
    total_momo = num_momo * 100
    total_mikan = num_mikan * 40
    total = total_momo + total_mikan
    print(name, '様', 'もも', num_momo, '個と、みかん', num_mikan, '個で', total, '円です。')

fruit_price(10, 40, 'Python.jp')
fruit_price(10, 40)
