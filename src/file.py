class File:
    def __init__(self):
        
        self.imports = {}
        self.structs = []
        

class Struct:
    def __init__(self, name, is_abstract, is_interface, indent):
        self.indent = indent
        self.name = name
        self.is_abstract = is_abstract
        self.is_interface = is_interface
        self.parents = []
        self.members = []
        #self.instance_fields = []
        #self.static_fields = []
        #self.methods = []
        #self.structs = []

class Enum:
    def __init__(self, name, indent):
        self.indent = indent
        self.name = name
        self.options = []


        
class Field:
    def __init__(self, name, visibility, value, is_static, indent):
        self.indent = indent
        self.name = name
        self.visibility = visibility
        self.value = value
        self.is_static = is_static



class Method:
    def __init__(self, name, visibility, is_abstract, is_static, params, body, indent):
        self.indent = indent
        self.name = name
        self.visibility = visibility
        self.is_abstract = is_abstract
        self.is_static = is_static
        self.params = params
        self.body = body

        
        
        


