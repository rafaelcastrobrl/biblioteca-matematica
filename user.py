import matematica as m

num = int(input('Informe um número para apresentar o seu fatorial: '))
resposta = m.fatorial(num)
print(resposta)
if m.primo(num):
    print('É primo!!')
else:
    print('Não é primo!!')

if m.par(num):
    print('É par!')
else:
    print('É impar!')