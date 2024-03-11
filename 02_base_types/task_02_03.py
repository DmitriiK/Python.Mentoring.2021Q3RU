condition_mapper = {3: 'Fizz', 5: 'Buzz'}

for x in range(100):
    out = ''
    for numb, label in condition_mapper.items():
        if x % numb == 0:
            out += label
        print(f'{x:3} -> {out}')
