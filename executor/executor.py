from serializer import serializer

class executor:
    def __init__(self,func,globals,locals):
        self.func = func
        self.locals = locals
        self.globals = globals
        for each in self.globals.items():
            setattr(self,each[0],each[1])
        self.result = None


    def run(self):
        self.result=self.func(*self.locals.get('args'),**self.locals.get('kwargs'))
