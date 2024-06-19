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


class Constructor:

    def __init__(self, params, body, indent):
        self.params = params
        self.body = body
        self.indent = indent


class ForLoop:

    def __init__(self, control, body, indent):
        self.indent = indent
        self.control = control
        self.body = body


class ForControl:

    def __init__(self, var, loop_range):
        self.var = var
        self.range = loop_range


class Switch:

    def __init__(self, var, cases, indent):
        self.indent = indent
        self.var = var
        self.cases = cases


class Case:

    def __init__(self, value, body, indent):
        self.indent = indent
        self.value = value
        self.body = body


class WhileLoop:

    def __init__(self, cond, body, indent):
        self.indent = indent
        self.cond = cond
        self.body = body


class IfCondition:

    def __init__(self, parts, indent):
        self.indent = indent
        self.parts = parts


class IfPart:

    def __init__(self, part_type, cond, body, indent):
        self.indent = indent
        self.part_type = part_type
        self.cond = cond
        self.body = body


class Line:

    def __init__(self, line, indent):
        self.line = line
        self.indent = indent
