


"""

Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?

"""



"""
def simpl_delitel():
    a = int(input('Cамый большой делитель числа: '))
    deliteli = []
    i = 1
    while i != a+1:
        if a % i == 0:
            deliteli.append(i)
        i += 1 
    return deliteli

if __name__ == "__main__":
    cat = simpl_delitel()
    print(cat)
    simpl_del = []
    for i in cat:
        a = 1
        timely_check = []
        while a != i+1:
            if i % a == 0:
                timely_check.append(a)
            a += 1
        if len(timely_check) == 2:
            if timely_check[0] == 1 and	timely_check[1] == i:
                simpl_del.append(i)	
    print(max(simpl_del))

"""



def simpl_delitel():
    a = int(input('Cамый большой делитель числа: '))
    i = a - 1
    while i != a+1:
        if a % i == 0:
            print(i)
            b = 1
            while b != i:
                if i % b == 0:
                    # end цикл закончить тут как нибудь 
                    if b == i and b == 1:
                        print('correct')
                    else:
                        print('not nided number')					
        i -= 1
	
    return 
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	