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
        self.non_static = []

    def check_for_non_static(self):
        for member in self.members:
            if type(member) == Field and not member.is_static:
                self.non_static.append(member)
                self.members.remove(member)



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

        
        
        


