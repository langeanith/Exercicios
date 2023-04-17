# 1047 - Tempo de Jogo com Minutos
hi, mi, hf, mf = map(int, input().split())

min, h = mf - mi, hf - hi
if min < 0:
    min += 60
    h -= 1
elif h == 0 and min == 0:
    h = 24
if h < 0:
    h += 24

print(f'O JOGO DUROU {h} HORA(S) E {min} MINUTO(S)')
