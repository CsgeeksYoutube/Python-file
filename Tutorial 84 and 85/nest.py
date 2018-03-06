import contextlib
@contextlib.contextmanager
def nest_test(name):
    print('entering',name)
    yield name
    print('exiting',name)