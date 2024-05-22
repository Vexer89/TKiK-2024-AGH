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



def convert(input_text):
    input_stream = InputStream(input_text)
    lexer = java_grammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = java_grammarParser(token_stream)
    tree = parser.program()

    converter = JtoPConverter()
    result = converter.visit(tree)

    return result

    converter = MyConverter()

    return result
