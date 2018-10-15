import math

masX = []
masY = []

# inputmas = 0
n = 1

for i in range(19):
    print('Введите элемент массива', n)
    masX.append(int(input()))
    n += 1
    
for i in range(19):
    y = 0,5 * math.log(masX[i])
    masY.append(y)
    
MaxY = masY[0]

for i in range(19):
    if masY[i]>MaxY:
        MaxY = masY[i]
        
print(MaxY)
