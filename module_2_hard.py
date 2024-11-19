def password(n):
    result=[]
    for i in range(1, n):
        if 3 <i>20:
            continue
        for j in range(i+1, n):
            if n % (i+j)== 0:
                 result.append((i,j))
    stroka=""
    for i,j in result:
        stroka+=str(i)+str(j)
    return stroka
n = int(input("Введите число от 3 до 20: "))
x= password(n)
print("Пароль: ", x)
