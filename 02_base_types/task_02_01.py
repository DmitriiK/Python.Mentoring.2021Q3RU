import fractions


def add_fractions():
    inp1 = input('Print first fraction,'
                 ' using format {numerator}/{denominator} (1/2): ')
    inp2 = input('Print second fraction, using same format: ')
    fr1 = fractions.Fraction(inp1)
    fr2 = fractions.Fraction(inp2)
    result = fr1 + fr2
    print(f'{inp1} + {inp2} = {result}')


if __name__ == '__main__':
    add_fractions()
