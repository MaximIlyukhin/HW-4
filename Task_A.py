# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: если k = 2, то многочлены могут быть
# => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Задать степень k = '))
b = []
for i in range(-101, 101, 2):
    b.append(i)
for i in range(-100, 101, 2):
    b.append(i)
b = b[::-1]
c = []
for i in range(1, 201, 2):
    c.append(b[i])
for i in range(0, 201, 2):
    c.append(b[i])
c = c[::-1]
d = []
for i in range(0, 201, 2):
    d.append(c[i])
for i in range(1, 201, 2):
    d.append(c[i])
d = d[::-1]
e = []
for i in range(1, 201, 2):
    e.append(d[i])
for i in range(0, 201, 2):
    e.append(d[i])
e = e[::-1]
f = ''
for i in range(k, 0, -1):
    if e[i*k+10] == 0:
        continue
    elif e[i*k+10] > 0:
        if i == 1:
            f = f + ' + ' + str(e[i*k+10]) + '*x '
        elif i == k:
            f = f + str(e[i*k+10]) + '*x**' + str(i)
        else:
            f = f + ' + ' + str(e[i*k+10]) + '*x**' + str(i)
    else:
        if i == 1:
            f = f + ' ' + str(e[i*k+10]) + '*x '
        elif i == k:
            f = f + ' ' + str(e[i*k+10]) + '*x**' + str(i)
        else:
            f = f + ' ' + str(e[i*k+10]) + '*x**' + str(i)
if e[i*k+22] < 0:
    f = f + str(e[i*k+22]) + ' = 0'
else:
    f = f + '+ ' + str(e[i*k+22]) + ' = 0'

data = open('text_A.txt', 'w')
data.writelines(f)
data.close()
