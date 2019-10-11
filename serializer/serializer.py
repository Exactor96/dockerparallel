import dill

class serializer:
    def __init__(self):
        pass

    def serialize(self,obj):
        return dill.dumps(obj)

    def deserialize(self,serialized):
        return dill.loads(serialized)