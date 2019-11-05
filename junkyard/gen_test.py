from serializer.serializer import serializer
def colazz(num):
    res = []
    if num == 0:
        return 0
    if num == 1:
        return [1,]
    while num != 1:
        if num % 2 == 0:
            res.append(num)
            num /= 2
        elif num % 2 == 1:
            res.append(num)
            num = num * 3 + 1
    return res


def arg_gen(a):
    for i in range(a+1):
        yield i


import dill

s =serializer()
print(s.serialize(arg_gen))