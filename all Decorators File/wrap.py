import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()

    return noop_wrapper

@noop
def hello():
    "print a well knw msg"
    print('hello world')