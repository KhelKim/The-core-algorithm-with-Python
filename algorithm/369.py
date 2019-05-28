num1 = 9871020
num2 = 5
num2 = str(num2)
count = 0
for i in range(num1):
    string = str(i)
    component = list(string)
    for j in component:
        if j == num2:
            count += 1
    if i % 100000 == 0:
        print('휴우')
print(count)
