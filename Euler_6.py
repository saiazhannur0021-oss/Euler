


"""


Сумма квадратов первых десяти натуральных чисел равна
12 + 22 + ... + 102 = 385

Квадрат суммы первых десяти натуральных чисел равен
(1 + 2 + ... + 10)2 = 552 = 3025

Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.

Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

"""


def only_plus_natural():
    a = int(input(f'enter number to 1^2 + 2^2 + .... to your nuber : '))
    sum_of_natural = 0
    i = 0
    while i != a+1:
        sum_of_natural += i * i
        i += 1
    return sum_of_natural
	
def only_plus_not_natural():
    b = int(input(f'enter number to 1^2 + 2^2 + .... to your nuber : '))
    sum_of_not_natural = 0
    i = 0
    while i != b+1:
        sum_of_not_natural += i 
        i += 1
    return sum_of_not_natural * sum_of_not_natural
	
	

cat1 = only_plus_natural()
cat2 = only_plus_not_natural()
print(f" {cat2} - {cat1} =", cat2 - cat1)

















