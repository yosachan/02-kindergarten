values = [10, 20, 30, 40, 55]
print(values[0] + values[2])
values = (10, 20, 30, 40, 55)
print(values[0] + values[2])
values = 'HELLO'
print(values[0] + values[2])
list1 = ['a', 'b', 'c']
list2 = ['a', 'b', 'd']
print(list1 <= list2)
list3 = ['a', 'b', 'c']
list4 = ['a', 'b', 'b']
print(list3 <= list4)
value1 = [1, 2, 3]
value2 = [1, 2, 3, 4]
print(value1 <= value2)
list_obj = [1, 2, 3]
var1, var2, var3 = list_obj
print(var1, var2, var3)
var1, var2, var3 = (1, 2, 3)
print(var1, var2, var3)
var1, var2, var3 = 'abc'
print(var1, var2, var3)
# cases = [100, 200, 300, 400, 500, 600, 700]
# total = 0
# for case_day in cases:
#     total += case_day
# avg = total / len(cases)
# print(total, avg)
def total_avg(values):
    total = 0
    for case_day in values:
        total += case_day
    num = len(values)
    avg = total / num
    return(total, avg)
values = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
total, avg = total_avg(values)
print(total, avg)
def total_avg_num(values):
    total = 0
    for case_day in values:
        total += case_day
    num = len(values)
    avg = total / num
    return(total, avg, num)
values = [1100, 1200, 1300, 1400, 1500, 1600, 1700]
total, avg, num = total_avg_num(values)
print(total, avg, num)





