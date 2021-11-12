lar = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))

a = (lar * alt)
t = a / 2

print('Sua aparede de a dimensão de {} X {} e sua área e de {:.1f}m² '.format(
    lar, alt, a))
print(
    'Para pintar essa parede voce prescisará de {:.1f}l de tinta. '.format(t))
