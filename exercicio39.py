print('A quantia de R$ 780_000.00 será dividida entre três ganhadores onde:'
      'o primeiro receberá 46%, '
      'o segundo receberá 32% e'
      'o terceiro receberá o restante, Quanto cada um irá gamahr?')
g1 = 780_000.00 * (46 / 100)
g2 = 780_000.00 * (32 / 100)
g3 = 780_000.00 - g1 - g2
print(f'O primeiro ganhador receberá: {g1:.2f}, o segundo ganhador receberá: {g2:.2f} '
      f'e o terceiro ganhador receberá: {g3:.2f}')