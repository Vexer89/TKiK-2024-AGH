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

        result = ""

        if struct.is_abstract or struct.is_interface:
            struct.parents.append("ABC")

        result += struct.indent * '\t'
        result += f"class {struct.name}({', '.join(struct.parents) if len(struct.parents) > 0 else ''}):\n"

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
        if method.is_abstract:
            result += "@abstractmethod \n"

        print(method.body)
        result += f"{converted_visibility}{method.name}({','.join(method.params) if len(method.params) > 0 else ''}):\n" \
                  f"{method.body}"

        return result

    def build_constructor(self, non_static, constructor):
        result = ""

        return result



