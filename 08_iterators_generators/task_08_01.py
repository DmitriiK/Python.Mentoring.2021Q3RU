def myzip(*args):
    # len_args = [len(arg) for arg in args]
    args_it = [iter(arg) for arg in args]
    # list of iterators for passed arguments
    while len(args_it) > 0:
        exhausted = list()
        for ind, arg_it in enumerate(args_it):
            try:
                next_itm = next(arg_it)
                yield next_itm
            except StopIteration:
                exhausted.append(ind)
        for ind in reversed(exhausted):
            # excluding exhausted from next iteration
            del args_it[ind]
