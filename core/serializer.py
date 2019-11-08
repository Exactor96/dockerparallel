import cloudpickle

class serializer:
    def __init__(self):
        pass

    def serialize(self,obj):
        return cloudpickle.dumps(obj)

    def deserialize(self,serialized):
        return cloudpickle.loads(serialized)