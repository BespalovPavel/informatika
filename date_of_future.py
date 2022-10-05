from datetime import datetime, timedelta

try:
    print('Введите дату дня рождения в формате ДД/ММ/ГГ')
    start_date = datetime.strptime(input(), "%d/%m/%y")
except:
    print('Дата в неверном формате')
    exit()

first = 10000
second = 1000000
third = 100000000
x = start_date+timedelta(days=first)
y = start_date+timedelta(minutes = second)
z = start_date+timedelta(seconds=third)

print("Дата с учётом изменеий")
print(x.day, y.day, z.day)
