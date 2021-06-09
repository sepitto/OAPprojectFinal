# Перевод в СИ

inches = 'inches'
lbs = 'lbs'
def perevod(znachenie, razmernost):
    if razmernost == 'inches':
        znachenie = znachenie * 0.0254
    elif razmernost == 'lbs':
        znachenie = znachenie * 0.453592
    return znachenie

# print(perevod(znachenie = 1, razmernost = inches))
# print(perevod(znachenie = 1, razmernost = lbs))

# Число узлов, число элментов, массив координат узлов, массив длин элементов

length = []
L = 0

def uzlovie_coordinates():
    with open("input File.txt", "r") as f:
        for line in f:
            if line[slice(0,4)] == 'GRID':
                arr = line.split(' ')
                arr = [x for x in arr if x != '']
                L = arr[2]
                L1 = L.split('.')
                if L1[1] == '':
                    L1[1] = '0'
                L = int(L1[0]) + int(L1[1])/10**(len(L1[1]))
                length.append(L)
    return length

uzlovie_coordinates()

uz_num = len(length)
el_num = len(length)-1

el_length = []

def arr_of_lengths():
    for i in range(1, len(length)):
        el_length.append(length[i] - length[i-1])
    return el_length

arr_of_lengths()

print('Число узлов', uz_num)
print('Число элементов', el_num)
print('Координаты узлов', length)
print('Длины элементов', el_length)

# Массив площадей сечений элементов

sechenie = []
F = 0

def arr_sechenie():
    with open("input File.txt", "r") as f:
        for line in f:
            if line[slice(0,4)] == 'PROD':
                arr = line.split(' ')
                arr = [x for x in arr if x != '']
                F = arr[3]
                F1 = F.split('.')
                if F1[1] == '':
                    F1[1] = '0'
                F = int(F1[0]) + int(F1[1])/10**(len(F1[1]))

                sechenie.append(F)
    return sechenie

arr_sechenie()

print(sechenie)

# Массив модулей упроугости 1-го рода элементов

mod_upr = []
E = 0

def arr_mod_upr():
    with open("input File.txt", "r") as f:
        for line in f:
            if line[slice(0,3)] == 'MAT':
                arr = line.split(' ')
                arr = [x for x in arr if x != '']
                E = arr[2]
                E1 = E.split('.')
                E1[1] = E1[1].split('E')
                if E1[1][0] == '':
                    E1[1][0] = '0'
                E = (int(E1[0]) + int(E1[1][0])/10**(len(E1[1][0]))) * 10 ** (int(E1[1][1]))
                mod_upr.append(E)
    return mod_upr

arr_mod_upr()

print(mod_upr)

# Массив жесткостей
EF = 0
gestkosti = []
for i in range(el_num):
    gestkosti.append([])

def arr_gestkosti():
    for i in range(el_num):
        for j in range(el_num):
            EF = mod_upr[0] * sechenie[0]
            gestkosti[i] = EF
    return gestkosti

arr_gestkosti()

print(gestkosti)

# Массив усилиий

usiliya = [float(0) for x in range(uz_num)]
U = 0
uzel = 0

def arr_usiliy():
    with open("input File.txt", "r") as f:
        for line in f:
            if line[slice(0, 5)] == 'FORCE':
                arr = line.split(' ')
                arr = [x for x in arr if x != '']
                U = arr[3]
                napravlenie = arr[4]
                napravlenie = napravlenie.split('.')
                if napravlenie[1] == '':
                    napravlenie[1] = '0'
                napravlenie = int(napravlenie[0]) + int(napravlenie[1]) / 10 ** (len(napravlenie[1]))
                uzel = int(arr[2]) - 1
                U1 = U.split('.')
                if U1[1] == '':
                    U1[1] = '0'
                U = int(U1[0]) + int(U1[1]) / 10 ** (len(U1[1]))
                usiliya[uzel] = U * napravlenie
    return usiliya

arr_usiliy()

print(usiliya)
