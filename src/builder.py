import file

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

                result += f"class {struct.name}(Enum):\n"
                elements = ""
                i = 1
                for el in struct.options:
                    elements += f"\t {el} = {i} \n"
                    i += 1
                result += elements

            elif type(struct) == file.Struct:
                result += f"class {struct.name}:"

        return result