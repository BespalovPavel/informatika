from random import *

a, b = 0, 0
print("Выберем, кто ходит первым")
cnt = randint(0, 1)
if cnt:
    print("Вы ходите первыми")
else: print("Система ходит первой")

n = randint(4,30)
print("Всего в куче ", n, " камней")
while n > 1:
    if cnt:
        stones = int(input("Ведите сколько камней Вы взяли: "))
        n -= stones
        a += stones
    else:
        if n < 4:
            stones = n - 1
        else:
            stones = randint(1, 3)
        print("Система выбирает: ", stones)
        n -= stones
        b += stones
    print("Ваше количество камней: ",a)
    print("Количество камней у системы: ", b)
    print("Осталось ", n, "камней")
    print()
    cnt = 1-cnt
if n:
    if 1-cnt:
        print("Вы выиграли")
    else:
        print("Система выиграла")
else:
    if cnt:
        print("Вы выиграли")
    else:
        print("Система выиграла")




