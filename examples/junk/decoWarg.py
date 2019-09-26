def deco(args):
    print(args)
    def wrap(func):
        print('wrap')
        func()
    return wrap

@deco('arg1')
def hello():
    print('hello')



hello()

