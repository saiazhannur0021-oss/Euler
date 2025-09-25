


"""

Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.


"""

i = 0
num_all = []

while i < 2000000:
    timely_arr = []
    for a in range(1, i):
        if i % 2 == 0:
            break
        elif i % a == 0:
            timely_arr.append(a)
            if a == 1:
                timely_arr.append(i)
        if len(timely_arr) == 3:
            break
    if len(timely_arr) == 2:
        if timely_arr[0] == 1 and timely_arr[1] == i:
            num_all.append(i)
    i += 1
	
print(sum(num_all))



