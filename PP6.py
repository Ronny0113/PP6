while True:  # ввод количества критериев и обработчик ошибки ввода
    try:
        n = int(input('Введите количество критериев: '))
        break
    except ValueError:
        print("Введите цифру!")
a = [0] * n  # делаем "строки" матрицы
ans = [0] * n
ost = 0
for i in range(n):  # делаем "столбцы" матрицы
    a[i] = [0] * n
for j in range(n):  # цикл для заполнения матрицы нашими значениями
    for i in range(n):
        if i == j:
            a[i][j] = 1
        elif j < i:
            while True:
                try:
                    b = int(input('Введите на сколько признак ' + str(j + 1) + ' важнее признака ' + str(i + 1) + ': '))
                    break
                except ValueError:
                    print("Введите цифру!")
            a[i][j] = b
        elif j > i:
            a[i][j] = 1/a[j][i]
        ans[j] += a[i][j]
        ost += a[i][j]
check = [0] * n
ost_check = 0
for i in range(n):  # округление чисел до сотых
    check[i] = ans[i]/ost
    check[i] = round(check[i], 2)
    ost_check += check[i]

while ost_check != 1:  # проверка на сумму ответов равную единице, и если не так, способ её решения
    if ost_check < 1:
        v = check.index(max(check))
        check[v] += 0.01
        ost_check += 0.01
    if ost_check > 1:
        v = check.index(max(check))
        check[v] -= 0.01
        ost_check -= 0.01

print('Весовые коэффициенты: ')  # вывод ответа
for i in range(n):
    print(check[i], end=' ')
