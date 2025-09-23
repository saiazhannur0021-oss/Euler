




def fiba():
    arr_fiba = []
    a = 1
    b = 2
    c = 0
    while b <= 4000000:# 1 + 2 = 3      2 + 3 = 5   3 + 5 = 8
        if b < 4000000:
            arr_fiba.append(b)
        c = b
        b = a + b
        a = c
    return arr_fiba


if __name__ == "__main__":
    cat = fiba()
    fiba_sum = 0
    for i in cat:
        if i % 2 == 0:
            fiba_sum += i
            print(fiba_sum)








