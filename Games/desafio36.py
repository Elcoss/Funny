v=float(input('Qual o valor da casa: R$'))
s=float(input('Quanto vc ganha de salario: R$'))
t=int(input('Quantos anos de financiamento: '))
s30=(s/100)*30
vt=(t*12)
vc=(v/vt)
print(f'Para pagar a casa de {v:.2f} em {t} a presta;ao sera de {vc:.2f}')
if vc>s30:
    print('Emprestimo negado!')
elif vc<=s30:
    print('Emprestimo consedido!')