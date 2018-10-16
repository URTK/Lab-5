import math

masX = []
masY = []

n = 1

    # Массив X

for i in range(19):
    print('Введите элемент массива', n)
    masX.append(int(input()))
    n += 1
print(' MasX ', masX)

    # Массив Y

for i in range(19):
    y = 0,5 * math.log(masX[i])
    masY.append(y)
print(' MasY ', masY)  

    # Поиск наибольшего числа, кратного 3 и вывод его индекса
    
MaxY = masY[0]

for i in range(19):
    if masY[i]>MaxY:
        MaxY = masY[i]
        if MaxY / 3 % 10
        
print(' Наивысший элемент ', MaxY)
