import functools
from typing import Callable


def fabric(lambda_to_apply_to_return: Callable) -> Callable:
    fabric.switched_on = True

    def decorator(primary_dec):

        @functools.wraps(primary_dec)
        def decorator_wrapper(primary_dec_param):
            # parameters for primary decorator

            def wrapper(f0):
                # f0 - initial function where we want to apply decorators
                @functools.wraps(f0)
                def ta_da_da_daam(*args, **kwargs):  # here the main play occurs
                    before_lambda = \
                        primary_dec(primary_dec_param)(f0)(args, kwargs)
                    output = lambda_to_apply_to_return(before_lambda)
                    return output

                return ta_da_da_daam

            return wrapper

        return decorator_wrapper

    return decorator


@fabric(lambda numb: numb ** 2)
def repeat(times):
    # here we are in "decorator factory"
    print('repeat')

    def decorator(func):
        # here we are producing "decorated(wrapped) functions
        print('repeat.decorator')

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('repeat.decorator.wrapper')
            total = 0
            for _ in range(times):
                inner_output = func(*args, **kwargs)
                total += inner_output
            return total / times

        return wrapper if fabric.switched_on else func

    return decorator


@repeat(3)
def foo(*args, **kwargs):
    print('Foo called!')
    return 3

# print(foo())
# repeat = fabric(lambda numb: numb ** 2)(repeat)
# foo = repeat(3)(foo)


print(foo())
fabric.switched_on = False
print(foo())
