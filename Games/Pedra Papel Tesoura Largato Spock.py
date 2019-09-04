//Sao importados as bibliotecas
from random import randint
from time import sleep
//Aqui sao mostradas as escolhas possiveis
print('''Suas Escolhas:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
[ 3 ] Lagarto
[ 4 ] Spock
[ 5 ] Regras''')
//o jogador faz uma escolha
j=int(input('Qual a sua jogada? '))
//se a escolha por =5 as regras sao exibidas
if j==5:
    print('''O jogo de pedra, papel, tesoura, lagarto e spock funciona assim:
Tesoura corta papel 
Papel cobre pedra 
Pedra esmaga lagarto 
Lagarto envenena Spock 
Spock esmaga (ou derrete) tesoura
Tesoura decapita lagarto 
Lagarto come papel 
Papel refuta Spock 
Spock vaporiza pedra 
Pedra quebra tesoura''')
//se a escolha for maior q 5 ou menor q 0 um erro e exibido
if j>=6 or j<0:
    print('Escolha um numero de 0 a 5')
//aqui o jogador faz a sua escolha
if j>=0 and j<5:
    o=('Pedra','Papel','Tesoura','Largato','Spock')
//aqui a maquina faz a sua escolha
    c=randint(0,4)
//aqui monstra ao jogador a escolha da maquina   
    print('Pedra, Papel')
    sleep(0.5)
    print('Tesoura')
    sleep(0.5)
    print('Lagarto, Spock')
    sleep(0.5)
    print('-='*11)
    print(f'Computador jogou {o[c]}')
    print(f'Jogador jogou {o[j]}')
    print('-='*11)
//aqui e determinado se o jogador venceu, empatou ou perdeu
    if j==0 and c== 2 or j==0 and c==3 or j==1 and c==0:
        print('JOGADOR VENCE')
    elif j==1 and c==4 or j==2 and c==1 or j==2 and c==3:
        print('JOGADOR VENCE')
    elif j==3 and c==1 or j==3 and c==4 or j==4 and c==2:
        print('JOGADOR VENCE')
    elif j==4 and c==0:
        print('JOGADOR VENCE')
    elif j==c:
        print('EMPATE')
    else:
        print('COMPUTADOR VENCE')
