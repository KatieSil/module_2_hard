n = int(input('Введите число от 3 до 20: '))
pairs_numbers = []
for i in range(1, 20) :
    if i < n :
        for j in range(i+1, 20) :
            a = i + j
            if n % a == 0 :
                pairs_numbers.append(i)
                pairs_numbers.append(j)

result = pairs_numbers
print('Нужный пароль, для введённого числа: ', *result, sep='')
# print('Нужный пароль, для введённого числа: ', *pairs_numbers)
