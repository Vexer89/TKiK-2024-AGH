import string

from gen.java_grammarLexer import java_grammarLexer
from gen.java_grammarParser import java_grammarParser
from gen.java_grammarVisitor import java_grammarVisitor
from antlr4 import *
import file
import builder


class JtoPConverter(java_grammarVisitor):
    def __init__(self):
        self.file = file.File()
        self.indentation_level = 0

    def add_to_imports(self, lib, cont):

        if lib not in self.file.imports:
            self.file.imports[lib] = []

        if cont not in self.file.imports[lib]:
            self.file.imports[lib].append(cont)

    def increase_indentation(self):
        self.indentation_level += 1

    def decrease_indentation(self):
        self.indentation_level -= 1

    def visitProgram(self, ctx):
        for element in ctx.importDeclaration() + ctx.packageDeclaration() + ctx.structerDeclaration():
            self.file.structs.append(self.visit(element))
        return self.file

    def visitImportDeclaration(self, ctx):
        import_name = ctx.extendedID().getText()
        self.file.imports[import_name] = None

    def visitPackageDeclaration(self, ctx):
        pass

    def visitStructerDeclaration(self, ctx):
        if ctx.classDeclaration():
            return self.visit(ctx.classDeclaration())
        elif ctx.interfaceDeclaration():
            return self.visit(ctx.interfaceDeclaration())
        elif ctx.enumDeclaration():
            return self.visit(ctx.enumDeclaration())

    def visitClassDeclaration(self, ctx):
        class_name = ctx.ID().getText()
        if ctx.classModifiers():
            modifiers = self.visit(ctx.classModifiers())
        else:
            modifiers = []

        if "abstract" in modifiers:
            is_abstract = True
            self.add_to_imports('abc', 'ABC')
        else:
            is_abstract = False

        new_class = file.Struct(class_name, is_abstract, False, self.indentation_level)

        if ctx.superClass():
            super_classes = self.visit(ctx.superClass())
        else:
            super_classes = []

        if ctx.interfaces():
            interfaces = self.visit(ctx.interfaces())
        else:
            interfaces = []

        new_class.parents = super_classes + interfaces

        for member in self.visit(ctx.classBody()):
            new_class.members.append(member)

        return new_class

    def visitClassModifiers(self, ctx):
        arr = []
        if "abstract" in ctx.getText():
            arr.append("abstract")
        if "default" in ctx.getText():
            arr.append("default")
        return arr

    def visitModifier(self, ctx):
        arr = []
        if "public" in ctx.getText():
            arr.append("public")
        if "private" in ctx.getText():
            arr.append("private")
        if "protected" in ctx.getText():
            arr.append("protected")
        if "static" in ctx.getText():
            arr.append("static")
        if "default" in ctx.getText():
            arr.append("default")
        return arr

    def visitInterfaceDeclaration(self, ctx):
        interface_name = ctx.ID().getText()
        self.add_to_imports('abc,' 'ABC')
        new_interface = file.Struct(interface_name, False, True, self.indentation_level)

        for member in self.visit(ctx.interfaceBody()):
            new_interface.members.append(member)

        return new_interface

    def visitEnumDeclaration(self, ctx):

        self.add_to_imports('enum', 'Enum')

        enum_name = ctx.ID().getText()
        new_enum = file.Enum(enum_name, self.indentation_level)

        for name in ctx.enumBody().ID():
            new_enum.options.append(name)

        return new_enum

    def visitSuperClass(self, ctx):
        names = []
        for name in ctx.ID():
            names.append(name.getText())
        return names

    def visitInterfaces(self, ctx):
        names = []
        for name in ctx.ID():
            names.append(name.getText())
        return names

    def visitClassBody(self, ctx):
        members = []
        self.increase_indentation()
        for member_node in ctx.classMemberDeclaration():
            member = self.visit(member_node)
            members.append(member)
        self.decrease_indentation()
        return members

    def visitClassMemberDeclaration(self, ctx):
        if ctx.fieldDeclaration():
            return self.visit(ctx.fieldDeclaration())
        elif ctx.methodDeclaration():
            return self.visit(ctx.methodDeclaration())
        elif ctx.classDeclaration():
            return self.visit(ctx.classDeclaration())
        elif ctx.interfaceDeclaration():
            return self.visit(ctx.interfaceDeclaration())
        elif ctx.enumDeclaration():
            return self.visit(ctx.enumDeclaration())
        elif ctx.constructor():
            return self.visit(ctx.constructor())

    def visitConstructor(self, ctx):
        name = ctx.ID().getText()
        params = self.visit(ctx.formalParameters()) if ctx.formalParameters() else []
        body = self.visit(ctx.methodBody())
        return file.Constructor(params, body, self.indentation_level)

    def visitFieldDeclaration(self, ctx):
        new_field = self.visit(ctx.variableDeclarators())
        modifiers = []
        if ctx.modifiers():
            for element in self.visit(ctx.modifiers()):
                modifiers.append(element.getText())

        if "public" in modifiers:
            new_field.visibility = 'public'
        elif "private" in modifiers:
            new_field.visibility = 'private'
        elif "protected" in modifiers:
            new_field.visibility = 'protected'

        if "static" in modifiers:
            new_field.is_static = True

        return new_field

    def visitModifiers(self, ctx):
        return ctx.modifier()

    def visitVariableDeclarators(self, ctx):
        field_name = ctx.ID().getText()

        if ctx.ASSIGN():
            field_value = ctx.literal().getText()
        else:
            field_value = None

        new_field = file.Field(field_name, None, field_value, False, self.indentation_level)

        return new_field

    def visitMethodDeclaration(self, ctx):
        method_name = ctx.ID().getText()

        params = self.visit(ctx.formalParameters()) if ctx.formalParameters() else []

        if ctx.ABSTRACT():
            is_abstract = True
            self.add_to_imports('abc,' 'abstractmethod')
        else:
            is_abstract = False

        modifiers = []
        if ctx.modifiers():
            for element in self.visit(ctx.modifiers()):
                modifiers.append(element)

        if "public" in modifiers:
            visibility = 'public'
        elif "private" in modifiers:
            visibility = 'private'
        elif "protected" in modifiers:
            visibility = 'protected'
        else:
            visibility = 'public'

        if "static" in modifiers:
            is_static = True
        else:
            is_static = False

        body = self.visit(ctx.methodBody())

        new_method = file.Method(method_name, visibility, is_abstract, is_static, params, body, self.indentation_level)

        return new_method

    def visitThrowedExeption(self, ctx):
        pass

    def visitFormalParameters(self, ctx):
        params = []
        for param in ctx.formalParameter():
            params.append(param.getText())
        return params

    def visitFormalParameter(self, ctx):
        param_name = ctx.ID().getText()
        return param_name

    # todo sprawdzić poniżej
    def visitMethodBody(self, ctx):
        return self.visit(ctx.block())

    def visitBlock(self, ctx):
        self.increase_indentation()
        print("ok")
        result = []
        print(ctx.statement())
        for statement in ctx.statement():
            obj = self.visit(statement)
            print(obj)
            result.append(obj)

        self.decrease_indentation()
        print(result)
        return result


    def visitStatement(self, ctx):
        print("ok2")
        if ctx.fullIfStatement():
            return self.visit(ctx.fullIfStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.doWhileStatement():
            return self.visit(ctx.doWhileStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.switchStatement():
            return self.visit(ctx.switchStatement())
        elif ctx.tryStatement():
            return self.visit(ctx.tryStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.breakStatement():
            return self.visit(ctx.breakStatement())
        elif ctx.continueStatement():
            return self.visit(ctx.continueStatement())
        elif ctx.throwStatement():
            return self.visit(ctx.throwStatement())
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.block():
            return self.visit(ctx.block())
        elif ctx.assignmentStatement():
            return self.visit(ctx.assignmentStatement())
        elif ctx.incrementStatement():
            return self.visit(ctx.incrementStatement())
        elif ctx.decrementStatement():
            return self.visit(ctx.decrementStatement())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.printStatement():
            return self.visit(ctx.printStatement())
        elif ctx.inputStatement():
            return self.visit(ctx.inputStatement())

    def visitFullIfStatement(self, ctx):
        parts = [self.visit(ctx.ifStatement())]
        for part in ctx.elseIfStatement():
            parts.append(self.visit(part))
        if ctx.elseStatement():
            parts.append(self.visit(ctx.elseStatement()))
        return file.IfCondition(parts, self.indentation_level)

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression())

        self.indentation_level += 1
        body = []
        for stmt in ctx.statement():
            body.append(self.visit(stmt))
        self.indentation_level -= 1

        new_if = file.IfPart("if", condition, body, self.indentation_level)

        return new_if

    def visitElseIfStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression())

        self.indentation_level += 1
        body = []
        for stmt in ctx.statement():
            body.append(self.visit(stmt))
        self.indentation_level -= 1

        new_if = file.IfPart("elif", condition, body, self.indentation_level)

        return new_if

    def visitElseStatement(self, ctx):
        body = []
        for stmt in ctx.statement():
            body.append(self.visit(stmt))

        new_if = file.IfPart("else", "", body, self.indentation_level)

        return new_if

    def visitWhileStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression())
        body = []
        for stmt in ctx.statement():
            body.append(self.visit(stmt))

        new_while = file.WhileLoop(condition, body, self.indentation_level)

        return new_while

    def visitDoWhileStatement(self, ctx):
        body = []
        for stmt in ctx.statement():
            body.append(self.visit(stmt))

        condition = self.visit(ctx.logicalExpression())
        body.append(file.Line(f"if {condition}:", self.indentation_level))
        body.append(file.Line(f"break", self.indentation_level + 1))

        new_while = file.WhileLoop("True", body, self.indentation_level)

        return new_while

    def visitForStatement(self, ctx):
        control = self.visit(ctx.forControl())

        body = []
        for stmt in ctx.statement():
            body.append(self.visit(stmt))

        new_for = file.ForLoop(control, body, self.indentation_level)

        return new_for

    def visitForControl(self, ctx):
        if ctx.enhancedForControl():
            return self.visit(ctx.enhancedForControl())
        elif ctx.traditionalForControl():
            return self.visit(ctx.traditionalForControl())

    def visitTraditionalForControl(self, ctx):
        # todo pomyslec nad bardziej złożonymi przypadkami
        var = self.visit(ctx.forInit())
        condition = self.visit(ctx.forCondition())

        new_control = file.ForControl(var, condition)
        return new_control

    def visitForInit(self, ctx):
        if ctx.assignmentStatement():
            return self.visit(ctx.assignmentStatement())
        elif ctx.extendedIDwithThis():
            return self.visit(ctx.extendedIDwithThis())

    def visitForCondition(self, ctx):
        # todo chujowo bo nie ma jak wydobyć literalu
        return self.visit(ctx.logicalExpression())

    def visitForUpdate(self, ctx):
        pass

    def visitEnhancedForControl(self, ctx):
        id_name = ctx.ID().getText()
        iterable = self.visit(ctx.extendedIDwithThis())
        new_control = file.ForControl(id_name, iterable)
        return new_control

    def visitSwitchStatement(self, ctx):
        var = self.visit(ctx.extendedIDwithThis())
        cases = []
        for case in ctx.switchBlock():
            cases.append(self.visit(case))

        new_switch = file.Switch(var, cases, self.indentation_level)

        return new_switch

    def visitSwitchBlockStatementGroup(self, ctx):
        values = []
        for value in ctx.switchLabel():
            values.append(self.visit(value))

        statements = []
        for stmt in ctx.statement():
            statements.append(self.visit(stmt))

        new_case = file.Case(values, statements, self.indentation_level)
        return new_case

    def visitSwitchLabel(self, ctx):
        if ctx.CASE():
            return self.visit(ctx.literal())
        elif ctx.DEFAULT():
            return None

    #todo obsługa błędów
    def visitTryStatement(self, ctx):
        try_block = self.visit(ctx.block())
        catches = "\n".join(self.visit(catch) for catch in ctx.catchClause())
        finally_block = f"\nfinally:\n{self.visit(ctx.finallyBlock())}" if ctx.finallyBlock() else ""
        return f"try:\n{try_block}{catches}{finally_block}"

    def visitCatchClause(self, ctx):
        param = self.visit(ctx.catchFormalParameter())
        block = self.visit(ctx.block())
        return f"except {param}:\n{block}"

    def visitCatchFormalParameter(self, ctx):
        id_name = ctx.ID().getText()
        return f"{id_name}"

    def visitFinallyBlock(self, ctx):
        return self.visit(ctx.block())
    #todo koniec obsługi błędów

    def visitReturnStatement(self, ctx):
        print("OK")
        if ctx.literal():
            ret_val = self.visit(ctx.literal())
        elif ctx.extendedIDwithThis():
            ret_val = self.visit(ctx.extendedIDwithThis())
        elif ctx.expression():
            print("expression")
            ret_val = self.visit(ctx.expression())

        if(type(ret_val) == file.Line):
            line = f"return {ret_val.line}"
        else:
            line = f"return {ret_val}"

        new_line = file.Line(line, self.indentation_level)
        print(new_line)
        return new_line

    def visitBreakStatement(self, ctx):
        new_line = file.Line(f"break", self.indentation_level)
        return new_line

    def visitContinueStatement(self, ctx):
        new_line = file.Line(f"continue", self.indentation_level)
        return new_line

    #todo obsługa błędów
    def visitThrowStatement(self, ctx):
        throw_expr = self.visit(ctx.ID() or ctx.newInstance())
        return f"raise {throw_expr};"
    #todo koniec obsługi błędów

    def visitExpression(self, ctx):
        print("ok3")
        if ctx.arithmeticExpression():
            print("arithmetic")
            return self.visit(ctx.arithmeticExpression())
        elif ctx.logicalExpression():
            print("logical")
            return self.visit(ctx.logicalExpression())

    def visitLogicalExpression(self, ctx):
        if ctx.logicalOperator():
            left = self.visit(ctx.logicalExpression())
            operator = self.visit(ctx.logicalOperator())
            right = self.visit(ctx.logicalTerm())
            new_line = file.Line(f"{left} {operator} {right}", self.indentation_level)
            return new_line
        else:
            print("else")
            new_line = file.Line(f"{self.visit(ctx.logicalTerm())}", self.indentation_level)
            return new_line

    def visitLogicalOperator(self, ctx):
        if ctx.LOGICAL_AND():
            return "and"
        elif ctx.LOGICAL_OR():
            return "or"
        else:
            ctx.getText()


    def visitLogicalTerm(self, ctx):
        if ctx.extendedIDwithThis():
            print("extended")
            return self.visit(ctx.extendedIDwithThis())
        elif ctx.literal():
            print("literal")
            return self.visit(ctx.literal())
        elif ctx.unaryLogicalExpression():
            return self.visit(ctx.unaryLogicalExpression())
        elif ctx.logicalExpression():
            print("logical")
            return f"({self.visit(ctx.logicalExpression())})"
        elif ctx.LPAREN() and ctx.RPAREN():
            print("paren")
            return f"({self.visit(ctx.arithmeticExpression())})"
        elif ctx.arithmeticExpression():
            print("arithmetic")
            return self.visit(ctx.arithmeticExpression())

    def visitUnaryLogicalExpression(self, ctx):
        return f"not {self.visit(ctx.logicalTerm())}"

    def visitArithmeticExpression(self, ctx):
        if ctx.arithmeticOperator():
            left = self.visit(ctx.arithmeticExpression())
            operator = ctx.arithmeticOperator().getText()
            right = self.visit(ctx.arithmeticTerm())
            new_line = file.Line(f"{left} {operator} {right}", self.indentation_level)
            return new_line
        else:
            new_line = file.Line(self.visit(ctx.arithmeticTerm()), self.indentation_level)
            return new_line

    def visitArithmeticTerm(self, ctx):
        if ctx.extendedIDwithThis():
            return self.visit(ctx.extendedIDwithThis())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.unaryArithmeticExpression():
            return self.visit(ctx.unaryArithmeticExpression())
        elif ctx.arithmeticExpression():
            return f"({self.visit(ctx.arithmeticExpression())})"

    def visitUnaryArithmeticExpression(self, ctx):
        operator = "+= 1" if ctx.ADD() else "-= 1"
        return f"{self.visit(ctx.arithmeticTerm())} {operator}"

    def visitAssignmentStatement(self, ctx) -> string:
        target = self.visit(ctx.extendedIDwithThis())
        value = self.visit(ctx.assignedValue())
        new_line = file.Line(f"{target} = {value}", self.indentation_level)
        return new_line

    def visitAssignedValue(self, ctx):
        if ctx.extendedIDwithThis():
            return self.visit(ctx.extendedIDwithThis())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.newInstance():
            return self.visit(ctx.newInstance())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.expression():
            return self.visit(ctx.expression())

    def visitLiteral(self, ctx):
        if ctx.INTEGER_NUMBER():
            return ctx.INTEGER_NUMBER()
        elif ctx.FLOAT_NUMBER():
            return ctx.FLOAT_NUMBER()
        elif ctx.STRING_TEXT():
            return ctx.STRING_TEXT()
        elif ctx.TRUE():
            return "True"
        elif ctx.FALSE():
            return "False"
        elif ctx.NULL():
            return "None"

    def visitExtendedID(self, ctx):
        return ctx.getText()

    def visitExtendedIDwithThis(self, ctx):
        if ctx.extendedID():
            if ctx.THIS():
                result = f"self.{ctx.extendedID().getText()}"
            else:
                result = ctx.extendedID().getText()
        else:
            result = "self"

        return result

    def visitDataType(self, ctx):
        return ctx.getText()

    def visitType(self, ctx):
        return ctx.getText()

    def visitFunctionCall(self, ctx):
        function_name = self.visit(ctx.extendedIDwithThis())
        arguments = ", ".join(self.visit(expr) for expr in ctx.extendedIDwithThis())
        new_line = file.Line(f"{function_name}({arguments})", self.indentation_level)
        return new_line

    def visitPrintStatement(self, ctx):
        if ctx.expression():
            out = self.visit(ctx.expression())
        elif ctx.literal():
            out = self.visit(ctx.literal())
        new_line = file.Line(f"print({out})", self.indentation_level)
        return new_line

    #todo tu w ogóle gramtyka jest zjebana
    def visitInputStatement(self, ctx):
        id_name = ctx.ID().getText()
        expression = self.visit(ctx.expression())
        return f"{id_name} = {ctx.SCANNER().getText()}({expression}).{ctx.NEXT().getText()}();"


def convert(input_text):
    input_stream = InputStream(input_text)
    lexer = java_grammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = java_grammarParser(token_stream)
    tree = parser.program()

    converter = JtoPConverter()
    file_obj = converter.visit(tree)
    new_builder = builder.PythonFileBuilder(file_obj)
    return new_builder.build()
