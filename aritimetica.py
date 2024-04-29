n1 = int (input('digite um número'))
n2 = int (input('digite outro valor'))

d = (n1/n2)
di = (n1//n2)
r = (n1%n2)
s = (n1+n2)
m = (n1*n2)
e = (n1** n2)

print ('='*20)
print ('A soma é {}, o produto é {}, o resto {} e a divisão é {:.3f}'.format(s, m, r, d), end=' ')
print ('Divisão inteiro {} e potência {}'.format(di, e))

print('========Desafio 05 =========')
ant=n1-1
suc=n1+1
print('numero digitado foi {} o seu antes é {} e o seu depois é {}'.format(n1, ant, suc))

print('========Desafio 06 =========')
print('o numero digitado foi', n1)
dobro = n1*2
triplo = n1*3
raiz = n1**(1/2)
print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {}'. format(n1, dobro, triplo, raiz))

print('========Desafio 07 =========')
n3 = float (input('digite um nota'))
n4 = float (input('digite outro nota'))
media= (n3+n4)/2
print('A média do aluno é{}'.format(media))

print('========Desafio 08 =========')
n5 = float (input('digite uma distância em metros = '))
centi= n5*100
mili= n5*1000
print('A distancia de {}metros em cm = {} e em mm é{}'.format(n5, centi, mili))

print('========Desafio 09 =========')
n6 = int (input('Informe valor para calcular a tabuada'))

n61 = n6*1
n62 = n6*2
n63 = n6*3
n64 = n6*4
n65 = n6*5
n66 = n6*6
n67 = n6*7
n68 = n6*8
n69 = n6*9
n610 = n6*10

print('=============TABUADA do {}',n6,' ==========')
print('{} * 0 = 0'.format(n6))
print('{} * 1 = {}'.format(n6, n61))
print('{} * 2 = {}'.format(n6, n62))
print('{} * 3 = {}'.format(n6, n63))
print('{} * 4 = {}'.format(n6, n64))
print('{} * 5 = {}'.format(n6, n65))
print('{} * 6 = {}'.format(n6, n66))
print('{} * 7 = {}'.format(n6, n67))
print('{} * 8 = {}'.format(n6, n68))
print('{} * 9 = {}'.format(n6, n69))
print('{} * 10 = {}'.format(n6, n610))

print('========Desafio 10 =========')
din = float(input('Valor em reais = '))
dol = din/4.95
print('Você pode comprar ${:.2f} dolares com o valor de R${:.2f}'.format(dol, din))

print('========Desafio 11 =========')
lar = float(input('Informe Largura = '))
alt = float(input('Informe Altura = '))
gasto1 = lar * alt
gasto2 = gasto1 / 2
print('Parede com {:.2f} metros quadrados, sendo necessáiro {:.2f} litros de tinta para pinta-lá'.format(gasto1, gasto2))

print('========Desafio 12 =========')
preco = float(input('preco do produto = '))
preco=preco-(preco*0.05)
print('Com desconto o preço fica R${:.2f}'.format(preco))

print('========Desafio 13 =========')
sal = float(input('Salário do colaborador = '))
sal=sal+(sal*0.15)
print('Salário com 15% de aumento = R${:.2f}'.format(sal))