"""

Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом?

"""

b = 1
i = 0
arr_simpl = []
while i != 7:
    for a in range(1, b+1):
        if b % a != 0:
            if b == a and b % 1 == 0:
                arr_simpl.append(b)
                i += 1
                break
    b += 1
	

print(arr_simpl)









