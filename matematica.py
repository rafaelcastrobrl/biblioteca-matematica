# fatorial
def fatorial(num):
    fat = 1
    while(num > 0):
        fat = fat * num
        num = num - 1
    return fat

# definir se o numero é primo ou não
def primo(num):
    div = 0
    valor = 1
    while valor <= num:
        if num%valor == 0:
            div = div + 1
        valor = valor + 1
    if div == 2:
        print('É primo!')
    else:
        print('Não é primo!')