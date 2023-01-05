# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

file_1 = open('B_1.txt')
a1 = file_1.readline()
file_1.close()
a = a1.replace(' ', '').replace('+', ' 0').\
    replace('-', ' -').replace('**', '0').replace('x0','X').\
        replace('*', ' ').replace('=0', '')
b = a.split()
# coun_1 - максимальная степень Х в 1-ом многочлене.
for i in range(len(b)-1, 0, -1):
    if 'X' in b[i]:
        coun_1 = b[i]
coun_1 = int(coun_1.replace('X', '')) 

file_2 = open('B_2.txt')
a2 = file_2.readline()
file_2.close()
c = a2.replace(' ', '').replace('+', ' 0').\
    replace('-', ' -').replace('**', '0').replace('x0','X').\
        replace('*', ' ').replace('=0', '')
d = c.split()
for i in range(len(d)-1, 0, -1):
    if 'X' in d[i]:
        coun_2 = d[i]
coun_2 = int(coun_2.replace('X', ''))
# coun - максимальная степень Х в 1-ом и в 2-ом многочленах.
if coun_1 >= coun_2:
    coun = coun_1
else:
    coun = coun_2
dict_1 = {}
# запись коэффициентов а0 и а1
if str(abs(int(b[len(b)-1]))).isdigit() and b[len(b)-2] == 'x':
    dict_1[0] = b[len(b)-1]
    dict_1[1] = b[len(b)-3]
elif not str(abs(int(b[len(b)-1]))).isdigit() and b[len(b)-1] == 'x':
    dict_1[0] = '0'
    dict_1[1] = b[len(b)-2]
elif str(abs(int(b[len(b)-1]))).isdigit() and not b[len(b)-2] == 'x':
    dict_1[0] = b[len(b)-1]
    dict_1[1] = '0'
# запись коэффициентов с а2 ...
for j in range(2, coun+1):
    for i in range(1, len(b), 2):
        if 'X' + str(j) == b[i]:
            dict_1[j] = b[i-1]
            break
    else:
        dict_1[j] = '0'
dict_2 = {}
if str(abs(int(d[len(d)-1]))).isdigit() and d[len(d)-2] == 'x':
    dict_2[0] = d[len(d)-1]
    dict_2[1] = d[len(d)-3]
elif not str(abs(int(d[len(d)-1]))).isdigit() and d[len(d)-1] == 'x':
    dict_2[0] = '0'
    dict_2[1] = d[len(d)-2]
elif str(abs(int(d[len(d)-1]))).isdigit() and not d[len(d)-2] == 'x':
    dict_2[0] = d[len(d)-1]
    dict_2[1] = '0'
for j in range(2, coun+1):
    for i in range(1, len(d), 2):
        if 'X' + str(j) == d[i]:
            dict_2[j] = d[i-1]
            break
    else:
        dict_2[j] = '0'
dict_3 = {}
for n in range(0, coun+1):
    dict_3[n] = int(dict_1[n]) + int(dict_2[n])
# печать первого, второго и финального многочлена с учетом отрицательных коэффициентов
print(a1, '+')
print(a2)
for i in range(coun, 1, -1):
    if int(dict_3[i]) > 0:
        print(' + ', dict_3[i], '*x**', i, sep='', end='')
    elif int(dict_3[i]) < 0:
        print(' ', dict_3[i], '*x**', i, sep='', end='')
if int(dict_3[1]) < 0:
    print(' ', dict_3[1], '*x', sep='', end='')
elif int(dict_3[1]) > 0:
    print(' + ', dict_3[1], '*x', sep='', end='')
if int(dict_3[0]) < 0:
    print(' ', dict_3[0], sep='', end='')
elif int(dict_3[0]) > 0:
    print(' + ', dict_3[0], sep='', end='')
print(' = 0', sep='', end='')
