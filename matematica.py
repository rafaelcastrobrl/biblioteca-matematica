# fatorial
# def fatorial(num):
#     fat = 1
#     while(num > 0):
#         fat = fat * num
#         num = num - 1
#     return fat
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fatorial(num - 1)

# definir se o numero é primo ou não
def primo(num):
    div = 0
    valor = 1
    while valor <= num:
        if num%valor == 0:
            div = div + 1
        valor = valor + 1
    if div == 2:
        return True
    else:
        return False

# Par ou não
# def par(num):
#     if num%2 == 0:
#         return True
#     else:
#         return False
def par(num):
    True if num%2 == 0 else False

# POTENCIA
def potquad(num):
    return num**2


    