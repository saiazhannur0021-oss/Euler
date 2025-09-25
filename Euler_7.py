"""

Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом?

"""

b = 1
i = 0
arr_simpl = []
arr_deli = []
while len(arr_simpl) != 100:
    arr_deli = []
    for a in range(1, i+1):
        if i % a == 0:
            arr_deli.append(a)
            if len(arr_deli) == 3:
                break 

    if len(arr_deli) == 2:
        if arr_deli[0] == 1 and	arr_deli[1] == i:
                arr_simpl.append(i)	 
                print(i)				
        				
    i += 1

print(arr_simpl)









