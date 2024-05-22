from output.java_grammarLexer import java_grammarLexer
from output.java_grammarParser import java_grammarParser
from output.java_grammarVisitor import java_grammarVisitor
from antlr4 import *


class JtoPConverter(java_grammarVisitor):

    def visitProgram(self, ctx):
        results = []
        for element in ctx.importDeclaration() + ctx.packageDeclaration() + ctx.structerDeclaration():
            result = self.visit(element)
            results.append(result)
        return "\n".join(results)

def visitImportDeclaration(self, ctx):
    import_name = ctx.extendedID().getText()
    return f"import {import_name}"

def visitPackageDeclaration(self, ctx):
    package_name = ctx.extendedID().getText()
    return ""

def visitClassDeclaration(self, ctx):
    class_name = ctx.ID().getText()
    superclass = f"({ctx.superClass().getText()})" if ctx.superClass() else ""
    interfaces = ", ".join(self.visit(interface) for interface in ctx.interfaces().ID()) if ctx.interfaces() else ""
    members = "\n".join(self.visit(member) for member in ctx.classBody().classMemberDeclaration())
    return f"class {class_name}{superclass}{interfaces}:\n{members}"

def convert(input_text):
    input_stream = InputStream(input_text)
    lexer = java_grammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = java_grammarParser(token_stream)
    tree = parser.program()

    converter = JtoPConverter()
    result = converter.visit(tree)

    return result