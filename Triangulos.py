# REFAÇA o desafio 35 (ex35.py), acrescentando que tipo de triângulo será formado

print("""Você deve me passar três comprimentos de retas para que o programa resolve dando
se é ou não possível de montar este triângulo que você que montar""")
c1 = float(input('Comprimento 1: '))
c2 = float(input('Comprimento 2: '))
c3 = float(input('Comprimento 3: '))

if c1 < (c2 + c3) and c2 < (c1 + c3) and c3 < (c2 + c1):
    print('É possível montar um triângulo com essas três retas')
    if c1 == c2 and c1 == c3 and c2 == c3:
        print('É um triângulo EQUILÁTERO')
    elif c1 == c2 or c1 == c3 or c2 == c3:
        print('É um triângulo ISÓSCELES')
    else:
        print('É um triângulo ESCALENO')
else:
    print('É impossível montar um triângulo com essas três retas')
    if c1 > c2 and c1 > c3:
        print(f'Devido ao {c1} ser muito grande')
    else:
        if c2 > c3 and c2 > c1:
            print(f'Devido ao {c2} ser muito grande')
        else:
            print(f'Devido ao {c3} ser muito grande')
