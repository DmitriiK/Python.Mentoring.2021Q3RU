from fractions import Fraction as Fr

numerator = 2 ** 12 + 4 * 6
denominator = 2 ** (3 / 8)
denominator_as_ratio = Fr(f'{2 * 8 + 3}/8')
print(f'as float = {numerator / denominator}')
print('as ratio = ' + str(Fr(f'{(numerator * denominator_as_ratio.denominator)}'
                             f'/{denominator_as_ratio.numerator}')))


num = pow(2, 12) + 4 * 6
den = pow(2, 3/8)
print(num/den)