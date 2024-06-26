import file


def convert_visibility(visibility):
    if visibility == "public":
        return ""
    elif visibility == "protected":
        return "_"
    elif visibility == "private":
        return "__"


class PythonFileBuilder:

    def __init__(self, file_obj: file.File):
        self.file_obj = file_obj

    def build(self):
        result = ""

        for key, value in self.file_obj.imports.items():
            if value is None:
                result += f"import {key} \n"
            else:
                items = ",".join(value)
                result += f"from {key} import {items} \n"

        for struct in self.file_obj.structs:
            if type(struct) == file.Enum:
                result += self.build_enum(struct)

            elif type(struct) == file.Struct:
                result += self.build_struct(struct)
                if struct.has_main:
                    result += f"{struct.name}.main()\n"

        return result

    def build_enum(self, struct):
        result = ""

        result += struct.indent * '\t'
        result += f"class {struct.name}(Enum):\n"

        elements = ""
        i = 1
        indent = struct.indent + 1
        tabs = indent * '\t'
        for el in struct.options:
            elements += f"{tabs}{el} = {i} \n"
            i += 1
        result += elements

        return result

    def build_struct(self, struct):

        constructor_exists = False
        result = ""

        if struct.is_abstract or struct.is_interface:
            struct.parents.append("ABC")

        result += struct.indent * '\t'
        if len(struct.parents) > 0:
            inheritance = f"({', '.join(struct.parents)})"
        else:
            inheritance = ''

        result += f"class {struct.name}{inheritance}:\n"

        struct.check_for_non_static()

        for member in struct.members:
            if type(member) == file.Enum:
                result += self.build_enum(member)
            elif type(member) == file.Struct:
                result += self.build_struct(member)
            elif type(member) == file.Field:
                result += self.build_static_field(member)
            elif type(member) == file.Method:
                result += self.build_method(member)
                if member.is_main:
                    struct.has_main = True
            elif type(member) == file.Constructor:
                constructor_exists = True
                result += self.build_constructor(struct.non_static, member)

        if not constructor_exists and struct.non_static:
            new_constructor = file.Constructor([], '', struct.indent + 1)
            result += self.build_constructor(struct.non_static, new_constructor)

        return result

    def build_static_field(self, field):
        result = ""
        result += field.indent * '\t'
        converted_visibility = convert_visibility(field.visibility)
        result += f"{converted_visibility}{field.name} = {field.value}\n"
        return result

    def build_method(self, method):
        result = ""
        converted_visibility = convert_visibility(method.visibility)

        result += method.indent * '\t'

        if method.is_static:
            result += "@staticmethod \n"
            result += method.indent * '\t'
        else:
            method.params.insert(0, "self")
        if method.is_abstract:
            result += "@abstractmethod \n"
            result += method.indent * '\t'
        result += f"def {converted_visibility}{method.name}({','.join(method.params) if len(method.params) > 0 else ''}):\n"
        result += self.build_body(method.body)

        return result

    def build_constructor(self, non_static, constructor):
        result = ""
        result += constructor.indent * '\t'

        undeclared_non_static = []
        for field in non_static:
            if field.name not in constructor.params:
                undeclared_non_static.append(f"{convert_visibility(field.visibility)}{field.name}")
        params_extended = constructor.params + undeclared_non_static

        result += f"def __init__(self, {','.join(params_extended) if len(params_extended) > 0 else ''}):\n "

        for name in undeclared_non_static:
            result += (constructor.indent + 1) * '\t'
            result += f"self.{name} = None \n"

        result += self.build_body(constructor.body)

        return result

    def build_for_loop(self, for_loop):
        result = ""
        result += for_loop.indent * '\t'
        result += f"for {for_loop.control.var} in {for_loop.control.range}:\n"
        result += self.build_body(for_loop.body)
        return result

    def build_while_loop(self, while_loop):
        result = ""
        result += while_loop.indent * '\t'
        result += f"while {while_loop.cond}:\n"
        result += self.build_body(while_loop.body)
        return result

    def build_if_condition(self, if_condition):
        result = ""
        for part in if_condition.parts:
            result += part.indent * '\t'
            result += f"{part.part_type} {part.cond}:\n"
            result += self.build_body(part.body)
        return result

    def build_line(self, line):
        return line + '\n'

    def build_switch(self, switch):
        result = ""
        is_first = True
        for case in switch.cases:
            result += case.indent * '\t'
            if is_first:
                if_type = "if"
                is_first = False
            else:
                if_type = "elif"
            if case.value is None:
                result += "else:\n"
            else:
                result += f"{if_type} {switch.var} == {case.value}:\n"

            for el in case.body:
                if type(el) == file.ForLoop:
                    result += self.build_for_loop(el)
                elif type(el) == file.WhileLoop:
                    result += self.build_while_loop(el)
                elif type(el) == file.IfCondition:
                    result += self.build_if_condition(el)
                elif type(el) == file.Switch:
                    result += self.build_switch(el)
                elif type(el) == str:
                    if "break" in el:
                        pass
                    else:
                        result += self.build_line(el)
                elif type(el) == file.TryCatch:
                    result += self.build_try_catch(el)

        return result

    def build_try_catch(self, el):
        result = ""

        result += el.indent * '\t'
        result += f"try:\n"
        result += self.build_body(el.try_block)

        for catch in el.catch_blocks:
            result += catch.indent * '\t'
            result += f"except {catch.exception}:\n"
            result += self.build_body(catch.body)

        if el.finally_block:
            result += el.indent * '\t'
            result += f"finally:\n"
            result += self.build_body(el.finally_block)
        return result


    def build_body(self, body):
        result = ""
        for el in body:
            if type(el) == file.ForLoop:
                result += self.build_for_loop(el)
            elif type(el) == file.WhileLoop:
                result += self.build_while_loop(el)
            elif type(el) == file.IfCondition:
                result += self.build_if_condition(el)
            elif type(el) == file.Switch:
                result += self.build_switch(el)
            elif type(el) == str:
                result += self.build_line(el)
            elif type(el) == file.TryCatch:
                result += self.build_try_catch(el)
        return result