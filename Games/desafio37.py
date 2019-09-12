n1=int(input('Digite um numero inteiro: '))
print('Escolha uma das bases de conversao: ')
print('[ 1 ] Converter para BINARIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
n2=int(input('Sua op;ao: '))
if n2==1:
    print(f'{n1} Convertido para Binario e {bin(n1)[2:]}')
elif n2==2:
    print(f'{n1} Convertido para Otal e {oct(n1)[2:]}')
elif n2==3:
    print(f'{n1} Convertido para Hexadecimal e {hex(n1)[2:]}')
else:
    print('Escolha um numero de 1 a 3')
