class File:
    def __init__(self):
        self.imports = {}
        self.structs = []

class Struct:
    def __init__(self, name, is_abstract, is_interface):
        self.name = name
        self.is_abstract = is_abstract
        self.is_interface = is_interface
        self.parents = []
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

        
        
        


