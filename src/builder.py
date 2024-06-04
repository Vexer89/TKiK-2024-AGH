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


        return result