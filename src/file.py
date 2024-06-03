class File:
    def __init__(self):
        self.imports = {}
        self.structs = []

class Struct:
    def __init__(self, st_type, visibility, is_abstract):
        self.st_type = st_type
        self.visibility = visibility
        self.is_abstract = is_abstract
        self.instance_fields = []
        self.static_fields = []
        self.methods = []
        self.structs = []

class Enum:
    def __init__(self, name):
        self.name = name
        self.options = []


        
class Field:
    def __init__(self, name, visibility, value):
        self.name = name
        self.visibility = visibility
        self.value = value



class Method:
    def __init__(self, return_type, name, visibility, is_abstract, body):
        self.return_type = return_type
        self.name = name
        self.visibility = visibility
        self.is_abstract = is_abstract
        self.params = []
        self.body = body

        
        
        


