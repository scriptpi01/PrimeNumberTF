quantity = int(input())
list = []
i = 0
while i < quantity:
    number = int(input())
    list.append(number)
    if list[i] % 2 !=0 or list[i] == 2:
        list[i] = 'T'
    else:
        list[i] = 'F'
    i += 1
print('\n'.join(list))