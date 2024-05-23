from gen.java_grammarLexer import java_grammarLexer
from gen.java_grammarParser import java_grammarParser
from gen.java_grammarVisitor import java_grammarVisitor
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
        return f"# package {package_name}"


    def visitStructerDeclaration(self, ctx):
        if ctx.classDeclaration():
            return self.visit(ctx.classDeclaration())
        elif ctx.interfaceDeclaration():
            return self.visit(ctx.interfaceDeclaration())
        elif ctx.enumDeclaration():
            return self.visit(ctx.enumDeclaration())


    def visitClassDeclaration(self, ctx):
        class_name = ctx.ID().getText()
        superclass = ("(" + ", ".join(self.visit(superclass) for superclass in ctx.superClass().ID()) + ")") if ctx.superClass() else ""
        #interfaces = ", ".join(self.visit(interface) for interface in ctx.interfaces().ID()) if ctx.interfaces() else ""
        members = "\n".join(self.visit(member) for member in ctx.classBody().classMemberDeclaration())
        return f"class {class_name}{superclass}:\n{members}"


    def visitInterfaceDeclaration(self, ctx):
        interface_name = ctx.ID().getText()
        members = "\n".join(self.visit(member) for member in ctx.interfaceBody().interfaceMemberDeclaration())
        return f"class {interface_name}:\n{members}"


    def visitEnumDeclaration(self, ctx):
        enum_name = ctx.ID().getText()
        enum_constants = ", ".join(ctx.enumBody().ID())
        members = "\n".join(self.visit(member) for member in ctx.enumBody().classMemberDeclaration())
        return f"enum {enum_name}({enum_constants}):\n{members}"


    def visitSuperClass(self, ctx):
        return ctx.getText()


    def visitInterfaces(self, ctx):
        return ", ".join(ctx.ID().getText() for id in ctx.ID())


    def visitClassBody(self, ctx):
        return "\n".join(self.visit(member) for member in ctx.classMemberDeclaration())


    def visitClassMemberDeclaration(self, ctx):
        if ctx.fieldDeclaration():
            return self.visit(ctx.fieldDeclaration())
        elif ctx.methodDeclaration():
            return self.visit(ctx.methodDeclaration())
        elif ctx.classDeclaration():
            return self.visit(ctx.classDeclaration())
        elif ctx.interfaceDeclaration():
            return self.visit(ctx.interfaceDeclaration())


    def visitFieldDeclaration(self, ctx):
        type_name = ctx.variableDeclarators().type_
        variables = ", ".join(self.visit(var) for var in ctx.variableDeclarators().ID()) if ctx.variableDeclarators().ID() else ""
        return f"{type_name} {variables};"


    def visitMethodDeclaration(self, ctx):
        method_name = ctx.ID().getText()
        params = self.visit(ctx.formalParameters()) if ctx.formalParameters() else ""
        body = self.visit(ctx.methodBody())
        return f"def {method_name}({params}):\n{body}"


    def visitThrowedExeption(self, ctx):
        return ", ".join(ctx.ID().getText() for id in ctx.ID())


    def visitFormalParameters(self, ctx):
        return ", ".join(self.visit(param) for param in ctx.formalParameter())


    def visitFormalParameter(self, ctx):
        type_name = ctx.type().getText()
        param_name = ctx.ID().getText()
        return f"{type_name} {param_name}"


    def visitMethodBody(self, ctx):
        return self.visit(ctx.block())


    def visitBlock(self, ctx):
        statements = "\n".join(self.visit(stmt) for stmt in ctx.blockStatement())
        return f"{{\n{statements}\n}}"


    def visitBlockStatement(self, ctx):
        return self.visit(ctx.statement())


    def visitVariableDeclarators(self, ctx):
        return ", ".join(self.visit(decl) for decl in ctx.ID())


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
            self.visit(expr) for expr in ctx.arithmeticExpression() + ctx.incrementStatement() + ctx.decrementStatement())


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
        return ".".join(ctx.ID())


    def visitExtendedIDwithThis(self, ctx):
        return ".".join(ctx.ID())


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
    result = converter.visit(tree)

    return result
