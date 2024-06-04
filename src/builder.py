import file

class PythonFileBuilder:

    def __init__(self, file_obj: file.File):
        self.file_obj = file_obj

    def build(self):
        result = ""

        for import_statement in self.file_obj.imports:
            pass






_