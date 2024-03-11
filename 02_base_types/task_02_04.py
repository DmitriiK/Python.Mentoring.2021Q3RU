# Greatest Common Divisor (GCD) of two integers A and B

def calc_GCD(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


if __name__ == '__main__':
    inp1 = input('Print first number not equal to zero: ')
    inp2 = input('Print second number  not equal to zero: ')
    GCD = calc_GCD(int(inp1), int(inp2))
    print(f'{GCD=}')
