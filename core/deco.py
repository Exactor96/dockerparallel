import dill

def serialize(func,_globals,_locals,path):
    dill.dump(dict({"func":func,"globals":_globals,"locals":_locals}),open(path,'wb'))


