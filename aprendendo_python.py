n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número: '))
s = n1+n2
print('A soma entre {0} e {1} é: {2}'.format(n1, n2, s))

//////////////////////////////////////////OUTRO PROGRAMA/////////////////////////////////////////////////////

a = input('Digite uma palavra: ')
print('O tipo primitivo desse valor é: {}'.format(type(a)))
print('Só tem espaços?',a.isspace())
print('É um número?',a.isnumeric())
print('É alfabético?',a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Está em maiúsculas?',a.isupper())
print('Está em minúsculas?',a.islower())
print('Está capitalizada?',a.istitle())

/////////////////////////////////////////OUTRO PROGRAMA/////////////////////////////////////////////////////

numero = int(input('Digite o número: '))
n1 = numero - 1
n2 = numero + 1
print('O número digitado foi o: {}. \nSeu antecessor é {} \nSeu sucessor é {}'.format(numero, n1, n2))

/////////////////////////////////////////OUTRO PROGRAMA////////////////////////////////////////////////////

numero = int(input('Digite o número que deseja: '))
n2=numero*2
n3=numero*3
n1=numero**(1/2)
print('O numero digitado foi o {}. \nO seu dobro é {}. \nSeu triplo é {}  \nSua raiz quadrada é {:.2f}.'.format(numero, n2, n3, n1))

////////////////////////////////////////OUTRO PROGRAMA//////////////////////////////////////////////////////

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media= (nota1+nota2)/2
print('Se sua primeira nota foi {:.1f}, e sua segunda nota foi {:.1f}. Sua média é {:.1f}'.format(nota1, nota2, media))

/////////////////////////////////////////OUTRO PROGRAMA////////////////////////////////////////////////////////

m= float(input('Digite a metragem desejada: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('{:.0f}m corresponde a {}km'.format(m, km))
print('{:.0f}m corresponde a {}hm'.format(m, hm))
print('{:.0f}m corresponde a {}dam'.format(m, dam))
print('{:.0f}m corresponde a {:.0f}dm'.format(m, dm))
print('{:.0f}m corresponde a {:.0f}cm'.format(m, cm))
print('{:.0f}m corresponde a {:.0f}mm'.format(m, mm))

/////////////////////////////////////////OUTRO PROGRAMA///////////////////////////////////////////////////////////

n = int(input('Digite algum número para saber sua tabuada: '))

print(12*'-')
print('{} x {:2} = {}'.format(n, 0, n*0))
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print(12*'-')

//////////////////////////////////////////OUTRO PROGRAMA////////////////////////////////////////////////////

real = float(input('Digite o quanto vocẽ tem em sua carteira: R$ '))
dolar = real/3.27
print('Se vocẽ tivver {:.2f} reais na carteira, poderá comprar U${:.2f}!'.format(real, dolar))

//////////////////////////////////////////OUTRO PROGRAMA//////////////////////////////////////////////////////

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
a = larg*alt
tinta = a/2
print('Sua parede tem {} m² logo, você precisará de {} litros de tinta para poder pintá-la'.format(a, qntdtin))

///////////////////////////////////////////OUTRO PROGRAMA////////////////////////////////////////////////////

preco = float(input('Digite o preço do produto: R$ '))
promo: float = preco*0.05
precofim = preco-promo
print('O produto de R${} na promoção de 5% de desconto vai para R${}'.format(preco, precofim))

///////////////////////////////////////////OUTRO PROGRAMA///////////////////////////////////////////////////

salin = float(input('Digite seu salário inicial: R$ '))
sal15 = salin*0.15
salfim = salin+sal15
print('O seu salário inicial era de R${:.2f}. Logo, com o aumento de 15% passará a ser R${:.2f}'.format(salin, salfim))

////////////////////////////////////////////////////////////////////////////////////////////////////////////

#sintam-se à vontade para me corrigirem e me darem dicas em o que posso melhorar.