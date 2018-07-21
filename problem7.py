num = 1
cont = 0
while cont <=10001:
    tot = 0
    for c in range(1, num+1):
        if num % c == 0:
            tot +=1
    if tot <=2 and num != 1:
        cont += 1
        if cont == 10001:
            print('O {}º número primo é: {}'.format(cont,num))
    num += 1
    if num > 100:
        print('teste')
    
