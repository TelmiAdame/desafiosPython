print('Escreva dois números inteiros e descubra qual deles é o maior:')
n1 = int(input('Escreva o primeiro número:'))
n2 = int(input('Escreva o segundo número:'))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois valores são iguais.')

#else/if/elif n1 == n2: