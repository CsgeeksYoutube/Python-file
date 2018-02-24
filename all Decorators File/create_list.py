def check(index):
    def validator(f):
        def wrap(*args):
            if args[index]<0:
                raise ValueError('argument {} must be non-neg'.format(index))
            return f(*args)
        return wrap
    return validator

@check(1)
def create_list(value, size):
    return [value]*size