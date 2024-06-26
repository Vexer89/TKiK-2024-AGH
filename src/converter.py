import string

from gen.java_grammarLexer import java_grammarLexer
from gen.java_grammarParser import java_grammarParser
from gen.java_grammarVisitor import java_grammarVisitor
from antlr4 import *
import file
import builder
import errors


class JtoPConverter(java_grammarVisitor):
    def __init__(self):
        self.file = file.File()
        self.indentation_level = 0
        self.declared_classes = []
        self.declared_interfaces = []
        self.declared_func = []
        self.declared_var = []

    def add_to_imports(self, lib, cont):

        if lib not in self.file.imports:
            self.file.imports[lib] = []

        if cont not in self.file.imports[lib]:
            self.file.imports[lib].append(cont)

    def increase_indentation(self):
        self.indentation_level += 1

    def decrease_indentation(self):
        self.indentation_level -= 1

    def getIndentation(self):
        return self.indentation_level * '\t'

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
        self.declared_classes.append(class_name)
        if ctx.classModifiers():
            modifiers = self.visit(ctx.classModifiers())
        else:
            modifiers = []

        if "abstract" in modifiers:
            is_abstract = True
            self.add_to_imports('abc', 'ABC')
        else:
            is_abstract = False

        members = []
        for member in self.visit(ctx.classBody()):
            members.append(member)

        new_class = file.Struct(class_name, is_abstract, False, members, self.indentation_level)

        if ctx.superClass():
            super_classes = self.visit(ctx.superClass())
        else:
            super_classes = []

        if ctx.interfaces():
            interfaces = self.visit(ctx.interfaces())
        else:
            interfaces = []

        new_class.parents = super_classes + interfaces

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
        self.declared_interfaces.append(interface_name)
        self.add_to_imports('abc', 'ABC')
        members = self.visit(ctx.interfaceBody())

        new_interface = file.Struct(interface_name, False, True, members, self.indentation_level)

        return new_interface

    def visitInterfaceBody(self, ctx):
        members = []
        self.increase_indentation()
        for member_node in ctx.interfaceMemberDeclaration():
            member = self.visit(member_node)
            members.append(member)
        self.decrease_indentation()
        return members

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
            if name.getText() not in self.declared_classes:
                raise Exception(f"Class {name.getText()} not declared")
            names.append(name.getText())
        return names

    def visitInterfaces(self, ctx):
        names = []
        for name in ctx.ID():
            if name.getText() not in self.declared_interfaces:
                raise Exception(f"Interface {name.getText()} not declared")
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
        self.declared_var.append(field_name)

        if ctx.ASSIGN():
            field_value = ctx.literal().getText()
        else:
            field_value = None

        new_field = file.Field(field_name, None, field_value, False, self.indentation_level)

        return new_field

    def visitMethodDeclaration(self, ctx):
        method_name = ctx.ID().getText()
        self.declared_func.append(method_name)

        params = self.visit(ctx.formalParameters()) if ctx.formalParameters() else []

        if ctx.ABSTRACT():
            is_abstract = True
            self.add_to_imports('abc', 'abstractmethod')
        else:
            is_abstract = False

        modifiers = []
        if ctx.modifiers():
            for element in self.visit(ctx.modifiers()):
                modifiers.append(element.getText())

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

        if ctx.methodBody():
            body = self.visit(ctx.methodBody())
        else:
            body = []

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
        return self.visit(ctx.block())

    def visitBlock(self, ctx):
        self.increase_indentation()
        result = []
        for statement in ctx.statement():
            obj = self.visit(statement)
            if type(obj) == str:
                obj = self.getIndentation() + obj
            result.append(obj)

        self.decrease_indentation()
        return result

    def visitStatement(self, ctx):
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

        self.increase_indentation()
        body = []
        for stmt in ctx.statement():
            obj = self.visit(stmt)
            if type(obj) == str:
                obj = self.getIndentation() + obj
            body.append(obj)
        self.decrease_indentation()

        new_if = file.IfPart("if", condition, body, self.indentation_level)

        return new_if

    def visitElseIfStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression())

        self.increase_indentation()
        body = []
        for stmt in ctx.statement():
            obj = self.visit(stmt)
            if type(obj) == str:
                obj = self.getIndentation() + obj
            body.append(obj)

        self.decrease_indentation()

        new_if = file.IfPart("elif", condition, body, self.indentation_level)

        return new_if

    def visitElseStatement(self, ctx):

        self.increase_indentation()
        body = []
        for stmt in ctx.statement():
            obj = self.visit(stmt)
            if type(obj) == str:
                obj = self.getIndentation() + obj
            body.append(obj)

        self.decrease_indentation()

        new_if = file.IfPart("else", "", body, self.indentation_level)

        return new_if

    def visitWhileStatement(self, ctx):
        condition = self.visit(ctx.logicalExpression())

        self.increase_indentation()
        body = []
        for stmt in ctx.statement():
            obj = self.visit(stmt)
            if type(obj) == str:
                obj = self.getIndentation() + obj
            body.append(obj)
        self.decrease_indentation()

        new_while = file.WhileLoop(condition, body, self.indentation_level)

        return new_while

    def visitDoWhileStatement(self, ctx):

        self.increase_indentation()
        body = []
        for stmt in ctx.statement():
            obj = self.visit(stmt)
            if type(obj) == str:
                obj = self.getIndentation() + obj
            body.append(obj)

        condition = self.visit(ctx.logicalExpression())
        body.append(f"{self.getIndentation()}if {condition}:")
        self.increase_indentation()
        body.append(f"{self.getIndentation()}break")
        self.decrease_indentation()
        self.decrease_indentation()

        new_while = file.WhileLoop("True", body, self.indentation_level)

        return new_while

    def visitForStatement(self, ctx):
        control = self.visit(ctx.forControl())

        self.increase_indentation()
        body = []
        for stmt in ctx.statement():
            obj = self.visit(stmt)
            if type(obj) == str:
                obj = self.getIndentation() + obj
            body.append(obj)
        self.decrease_indentation()

        new_for = file.ForLoop(control, body, self.indentation_level)

        return new_for

    def visitForControl(self, ctx):
        if ctx.enhancedForControl():
            return self.visit(ctx.enhancedForControl())
        elif ctx.traditionalForControl():
            return self.visit(ctx.traditionalForControl())

    def visitTraditionalForControl(self, ctx):

        var, start = self.visit(ctx.forInit())
        end = self.visit(ctx.forCondition())
        update = self.visit(ctx.forUpdate())
        condition = f"range({start}, {end}, {update})"

        new_control = file.ForControl(var, condition)
        return new_control

    def visitForInit(self, ctx):
        if ctx.assignmentStatement():
            as_str = self.visit(ctx.assignmentStatement())
            var_name, var_value = as_str.split(" = ")
            return [var_name, var_value]
        elif ctx.extendedIDwithThis():
            return self.visit(ctx.extendedIDwithThis())

    def visitForCondition(self, ctx):
        operators = ['<', '>', '==', '!=', '<=', '>=']
        as_str = self.visit(ctx.logicalExpression())
        for operator in operators:
            if operator in as_str:
                var_name, var_value = as_str.split(operator)
                return var_value.strip()
        return None

    def visitForUpdate(self, ctx):
        if ctx.incrementStatement():
            return 1
        elif ctx.decrementStatement():
            return -1

    def visitEnhancedForControl(self, ctx):
        id_name = ctx.ID().getText()
        iterable = self.visit(ctx.extendedIDwithThis())
        new_control = file.ForControl(id_name, iterable)
        return new_control

    def visitSwitchStatement(self, ctx):
        var = self.visit(ctx.extendedIDwithThis())
        cases = self.visit(ctx.switchBlock())

        new_switch = file.Switch(var, cases, self.indentation_level)

        return new_switch

    def visitSwitchBlock(self, ctx):
        cases = []
        for case in ctx.switchBlockStatementGroup():
            cases.append(self.visit(case))
        return cases

    def visitSwitchBlockStatementGroup(self, ctx):
        value = self.visit(ctx.switchLabel())

        self.increase_indentation()
        statements = []
        for stmt in ctx.statement():
            obj = self.visit(stmt)
            if type(obj) == str:
                obj = self.getIndentation() + obj
            statements.append(obj)
        self.decrease_indentation()

        new_case = file.Case(value, statements, self.indentation_level)
        return new_case

    def visitSwitchLabel(self, ctx):
        if ctx.CASE():
            return self.visit(ctx.literal())
        elif ctx.DEFAULT():
            return None

    def visitTryStatement(self, ctx):
        try_block = self.visit(ctx.block())

        catches = []
        for catch in ctx.catchClause():
            catches.append(self.visit(catch))

        finally_block = self.visit(ctx.finallyBlock()) if ctx.finallyBlock() else None

        return file.TryCatch(try_block, catches, finally_block, self.indentation_level)

    def visitCatchClause(self, ctx):
        param = self.visit(ctx.catchFormalParameter())
        block = self.visit(ctx.block())
        return file.CatchBlock(param, block, self.indentation_level)

    def visitCatchFormalParameter(self, ctx):
        exception = self.visit(ctx.type_())
        return exception

    def visitFinallyBlock(self, ctx):
        return self.visit(ctx.block())

    def visitReturnStatement(self, ctx):
        if ctx.literal():
            ret_val = self.visit(ctx.literal())
        elif ctx.extendedIDwithThis():
            ret_val = self.visit(ctx.extendedIDwithThis())
        elif ctx.expression():
            ret_val = self.visit(ctx.expression())

        return f"return {ret_val}"

    def visitBreakStatement(self, ctx):
        return f"break"

    def visitContinueStatement(self, ctx):
        return f"continue"

    def visitThrowStatement(self, ctx):
        if ctx.ID():
            throw_expr = ctx.ID().getText()
        elif ctx.newInstance():
            throw_expr = self.visit(ctx.newInstance())
        return f"raise {throw_expr};"

    def visitExpression(self, ctx):
        if ctx.arithmeticExpression():
            return self.visit(ctx.arithmeticExpression())
        elif ctx.logicalExpression():
            return self.visit(ctx.logicalExpression())

    def visitLogicalExpression(self, ctx):
        if ctx.logicalOperator():
            left = self.visit(ctx.logicalExpression())
            operator = self.visit(ctx.logicalOperator())
            right = self.visit(ctx.logicalTerm())
            return f"{left} {operator} {right}"
        else:
            return f"{self.visit(ctx.logicalTerm())}"

    def visitLogicalOperator(self, ctx):
        if ctx.LOGICAL_AND():
            return "and"
        elif ctx.LOGICAL_OR():
            return "or"
        elif ctx.EQUAL():
            return "=="
        elif ctx.NOT_EQUAL():
            return "!="
        elif ctx.GREATER_THAN():
            return ">"
        elif ctx.LESS_THAN():
            return "<"
        elif ctx.LESS_THAN_OR_EQUAL():
            return "<="
        elif ctx.GREATER_THAN_OR_EQUAL():
            return ">="

    def visitLogicalTerm(self, ctx):
        if ctx.extendedIDwithThis():
            return self.visit(ctx.extendedIDwithThis())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.unaryLogicalExpression():
            return self.visit(ctx.unaryLogicalExpression())
        elif ctx.logicalExpression():
            return f"({self.visit(ctx.logicalExpression())})"
        elif ctx.LPAREN() and ctx.RPAREN():
            return f"({self.visit(ctx.arithmeticExpression())})"
        elif ctx.arithmeticExpression():
            return self.visit(ctx.arithmeticExpression())

    def visitUnaryLogicalExpression(self, ctx):
        return f"not {self.visit(ctx.logicalTerm())}"

    def visitArithmeticExpression(self, ctx):
        if ctx.arithmeticOperator():
            left = self.visit(ctx.arithmeticExpression())
            operator = self.visit(ctx.arithmeticOperator())
            right = self.visit(ctx.arithmeticTerm())
            return f"{left} {operator} {right}"
        else:
            return f"{self.visit(ctx.arithmeticTerm())}"

    def visitArithmeticOperator(self, ctx):
        if ctx.ADD():
            return "+"
        elif ctx.SUB():
            return "-"
        elif ctx.MUL():
            return "*"
        elif ctx.DIV():
            return "/"
        elif ctx.MOD():
            return "%"

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
        operator = "+" if ctx.ADD() else "-"
        return f"{operator} {self.visit(ctx.arithmeticTerm())}"

    def visitAssignmentStatement(self, ctx) -> string:
        target = self.visit(ctx.extendedIDwithThis())
        value = self.visit(ctx.assignedValue())
        return f"{target} = {value}"

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

    def visitNewInstance(self, ctx):
        if ctx.dataStructerDeclaration():
            return self.visit(ctx.dataStructerDeclaration())
        else:
            class_name = ctx.ID().getText()
            if class_name not in self.declared_classes:
                raise Exception(f"Class {class_name} not declared")
            if ctx.parameters():
                params = self.visit(ctx.parameters())
            else:
                params = ""
            return f"{class_name}({params})"

    def visitDataStructerDeclaration(self, ctx):
        return self.visit(ctx.dataStructers())

    def visitDataStructers(self, ctx):
        if ctx.ARRAYLIST() or ctx.LINKEDLIST():
            return "[]"
        elif ctx.HASHMAP():
            return "{}"
        elif ctx.HASHSET():
            return "set()"

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

    def visitDecrementStatement(self, ctx):
        target = self.visit(ctx.extendedIDwithThis())
        return f"{target} -= 1"

    def visitIncrementStatement(self, ctx):
        target = self.visit(ctx.extendedIDwithThis())
        return f"{target} += 1"

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

        function_name_without_classes = function_name.split('.')[-1]
        if(function_name_without_classes not in self.declared_func):
            raise Exception(f"Function {function_name} not declared")
        if ctx.parameters():
            arguments = self.visit(ctx.parameters())
        else:
            arguments = ""
        return f"{function_name}({arguments})"

    def visitPararameters(self, ctx):
        return ", ".join(self.visit(param) for param in ctx.parameter())

    def visitParameter(self, ctx):
        if ctx.extendedIDwithThis():
            return self.visit(ctx.extendedIDwithThis())
        elif ctx.literal():
            return self.visit(ctx.literal())

    def visitPrintStatement(self, ctx):
        if ctx.expression():
            out = self.visit(ctx.expression())
        elif ctx.literal():
            out = self.visit(ctx.literal())
        return f"print({out})"

    def visitInputStatement(self, ctx):
        pass


def convert(input_text):
    input_stream = InputStream(input_text)
    lexer = java_grammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = java_grammarParser(token_stream)

    parser.removeErrorListeners()
    error_listener = errors.MyErrorListener()
    parser.addErrorListener(error_listener)

    try:
        tree = parser.program()
    except Exception as e:
        return str(e)

    converter = JtoPConverter()
    try:
        file_obj = converter.visit(tree)
    except Exception as e:
        return str(e)

    new_builder = builder.PythonFileBuilder(file_obj)
    return new_builder.build()
