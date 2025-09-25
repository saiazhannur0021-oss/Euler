


"""
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a^2 + b^2 = c^2

Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.

"""


def shorter_a_b_c(a, b, c):
    uslovie_abc = False
    if a < b and b < c:
        uslovie_abc = True
    return uslovie_abc

def a2_b2_c2(a, b, c):
    uslovie_abc = False
    a2 = a * a
    b2 = b * b
    c2 = c * c
    a2b2 = a2 + b2
    if a2b2 == c2:
        uslovie_abc = True
    return uslovie_abc

def plus_a_b_c(a, b, c):
    uslovie_abc = False
    a_b_c_1000 = a + b + c
    if a_b_c_1000 == 1000:
        uslovie_abc = True
    return uslovie_abc



if __name__ == "__main__":
    correct_abc_list = []
    print("start")
    for b in range(1, 1001):
        for a in range(1, 1001):
            c = 1000 - (a + b)
            if plus_a_b_c(a, b, c) == True and a2_b2_c2(a, b, c) == True and shorter_a_b_c(a, b, c) == True:
                correct_abc_text = (f"a = {a} and b = {b} and c = {c}")
                correct_abc_list.append(correct_abc_text)
                print(correct_abc_list)
    print(correct_abc_list)





