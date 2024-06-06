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

        print(lib)

        if lib not in self.file.imports:
            self.file.imports[lib] = []

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

    #todo zaimplementować konstruktor
    def visitConstructor(self, ctx):
        pass

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

    def visitMethodBody(self, ctx):
        self.increase_indentation()
        return self.visit(ctx.block())

    def visitBlock(self, ctx):
        statements = "\n".join(self.visit(stmt) for stmt in ctx.blockStatement())
        self.decrease_indentation()
        return f"{{\n{statements}\n}}"

    def visitBlockStatement(self, ctx):
        self.increase_indentation()
        return self.visit(ctx.statement())

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression() or ctx.arithmeticExpression())
        then_block = self.visit(ctx.statement(0))
        else_block = f"\nelse:\n{self.visit(ctx.statement(1))}" if ctx.statement(1) else ""
        return f"if {condition}:\n{then_block}{else_block}"

    def visitWhileStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression() or ctx.arithmeticExpression())
        body = self.visit(ctx.statement())
        return f"while {condition}:\n{body}"

    def visitDoWhileStatement(self, ctx):
        body = self.visit(ctx.statement())
        condition = self.visit(ctx.logicalExpression() or ctx.arithmeticExpression())
        return f"do:\n{body}\nwhile {condition};"

    def visitForStatement(self, ctx):
        control = self.visit(ctx.forControl())
        body = self.visit(ctx.statement())
        return f"for {control}:\n{body}"

    def visitForControl(self, ctx):
        if ctx.enhancedForControl():
            return self.visit(ctx.enhancedForControl())
        elif ctx.traditionalForControl():
            return self.visit(ctx.traditionalForControl())

    def visitTraditionalForControl(self, ctx):
        init = self.visit(ctx.forInit())
        condition = self.visit(ctx.logicalExpression())
        update = self.visit(ctx.forUpdate())
        return f"{init}; {condition}; {update}"

    def visitForInit(self, ctx):
        return self.visit(ctx.assignmentStatement() or ctx.extendedIDwithThis())

    def visitForUpdate(self, ctx):
        return ", ".join(
            self.visit(expr) for expr in
            ctx.arithmeticExpression() + ctx.incrementStatement() + ctx.decrementStatement())

    def visitEnhancedForControl(self, ctx):
        type_name = ctx.type().getText()
        id_name = ctx.ID().getText()
        iterable = self.visit(ctx.extendedIDwithThis())
        return f"{type_name} {id_name} in {iterable}"

    def visitSwitchStatement(self, ctx):
        switch_expression = self.visit(ctx.extendedIDwithThis())
        cases = "\n".join(self.visit(case) for case in ctx.switchBlock().switchBlockStatementGroup())
        return f"match {switch_expression}:\n{cases}"

    def visitSwitchBlockStatementGroup(self, ctx):
        labels = "\n".join(self.visit(label) for label in ctx.switchLabel())
        statements = "\n".join(self.visit(stmt) for stmt in ctx.block())
        return f"{labels}\n{statements}"

    def visitSwitchLabel(self, ctx):
        if ctx.CASE():
            return f"case {self.visit(ctx.literal())}:"
        elif ctx.DEFAULT():
            return "default:"

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
        type_name = ctx.type().getText()
        id_name = ctx.ID().getText()
        return f"{type_name} {id_name}"

    def visitFinallyBlock(self, ctx):
        return self.visit(ctx.block())

    def visitReturnStatement(self, ctx):
        expr = self.visit(ctx.expression()) if ctx.expression() else ""
        return f"return {expr};"

    def visitBreakStatement(self, ctx):
        return "break;"

    def visitContinueStatement(self, ctx):
        return "continue;"

    def visitThrowStatement(self, ctx):
        throw_expr = self.visit(ctx.ID() or ctx.newInstance())
        return f"throw {throw_expr};"

    def visitExpression(self, ctx):
        return self.visit(ctx.logicalExpression() or
                          ctx.arithmeticExpression() or
                          ctx.assignmentStatement() or
                          ctx.incrementStatement() or
                          ctx.decrementStatement() or
                          ctx.functionCall() or
                          ctx.printStatement() or
                          ctx.inputStatement()
                          )

    def visitLogicalExpression(self, ctx):
        if ctx.logicalOperator():
            left = self.visit(ctx.logicalTerm(0))
            operator = ctx.logicalOperator().getText()
            right = self.visit(ctx.logicalTerm(1))
            return f"{left} {operator} {right}"
        else:
            return self.visit(ctx.logicalTerm(0))

    def visitLogicalTerm(self, ctx):
        if ctx.logicalExpression():
            return f"({self.visit(ctx.logicalExpression())})"
        elif ctx.arithmeticExpression():
            return self.visit(ctx.arithmeticExpression())
        elif ctx.logicalOperator():
            return f"{ctx.logicalOperator().getText()} {self.visit(ctx.logicalTerm())}"
        elif ctx.logicalOperator() and ctx.logicalExpression():
            return f"{ctx.logicalOperator().getText()} {self.visit(ctx.logicalExpression())}"
        elif ctx.logicalOperator() and ctx.arithmeticExpression():
            return f"{ctx.logicalOperator().getText()} {self.visit(ctx.arithmeticExpression())}"
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

    def visitUnaryLogicalExpression(self, ctx):
        return f"{ctx.LOGICAL_NOT().getText()} {self.visit(ctx.logicalTerm())}"

    def visitArithmeticExpression(self, ctx):
        if ctx.arithmeticOperator():
            left = self.visit(ctx.arithmeticTerm(0))
            operator = ctx.arithmeticOperator().getText()
            right = self.visit(ctx.arithmeticTerm(1))
            return f"{left} {operator} {right}"
        else:
            return self.visit(ctx.arithmeticTerm(0))

    def visitArithmeticTerm(self, ctx):
        if ctx.arithmeticExpression():
            return f"({self.visit(ctx.arithmeticExpression())})"
        elif ctx.INCREMENT():
            return f"{self.visit(ctx.getChild(0))} {ctx.INCREMENT().getText()}"
        elif ctx.DECREMENT():
            return f"{self.visit(ctx.getChild(0))} {ctx.DECREMENT().getText()}"
        elif ctx.logicalExpression():
            return self.visit(ctx.logicalExpression())
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

    def visitUnaryArithmeticExpression(self, ctx):
        operator = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
        return f"{operator}{self.visit(ctx.arithmeticTerm())}"

    def visitAssignmentStatement(self, ctx):
        type_name = ctx.type().getText() if ctx.type() else ""
        target = self.visit(ctx.extendedIDwithThis())
        operator = ctx.assignmentOperator().getText()
        value = self.visit(
            ctx.expression() or ctx.newInstance() or ctx.extendedIDwithThis() or ctx.literal() or ctx.functionCall())
        return f"{type_name} {target} {operator} {value}"

    def visitLiteral(self, ctx):
        if ctx.INTEGER_NUMBER():
            return ctx.INTEGER_NUMBER().getText()
        elif ctx.FLOAT_NUMBER():
            return ctx.FLOAT_NUMBER().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
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
                result = f"self.{ctx.extendedID()}"
            else:
                result = ctx.extendedID()
        else:
            result = "self"

        return result

    def visitDataType(self, ctx):
        return ctx.getText()

    def visitType(self, ctx):
        return ctx.getText()

    def visitFunctionCall(self, ctx):
        function_name = self.visit(ctx.extendedIDwithThis())
        arguments = ", ".join(self.visit(expr) for expr in ctx.expression())
        return f"{function_name}({arguments})"

    def visitPrintStatement(self, ctx):
        print_type = "print" if ctx.PRINT() else "println"
        expr = self.visit(ctx.expression())
        return f"{print_type}({expr})"

    def visitInputStatement(self, ctx):
        type_name = ctx.type().getText()
        id_name = ctx.ID().getText()
        expression = self.visit(ctx.expression())
        return f"{type_name} {id_name} = {ctx.SCANNER().getText()}({expression}).{ctx.NEXT().getText()}();"


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
