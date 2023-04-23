berries = input("Введите количество ягод на кусте через пробел: ").split(" ")

result = 0
for i in range(len(berries) - 1):
    current = int(berries[i])
    next = 0
    prev = 0

    if(i == 0):
        next = int(berries[i + 1])
        prev = int(berries[len(berries) - 1]) 
    elif (i == len(berries) - 1):
        next = int(berries[0]) 
        prev = int(berries[i - 1])
    else:
        next = int(berries[i + 1])
        prev = int(berries[i - 1])
    buf =  prev + current + next
    
    if (buf > result):
        result = buf


print(result)