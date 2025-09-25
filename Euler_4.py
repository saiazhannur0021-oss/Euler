


"""


Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""




def polindrom():
    a = 999
    i = 100
    b = 100
    arr_polindrom = []
    while i != a+1:
        b = 100
        while b != a+1:
            c = b * i

            new_arr = list(str(c))
            if new_arr == new_arr[::-1]:
                arr_polindrom.append(c)
            b += 1
        i += 1
    return arr_polindrom







if __name__ == "__main__":
    a = polindrom()
    print(max(a))






