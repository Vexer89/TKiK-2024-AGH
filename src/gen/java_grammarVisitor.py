# Generated from grammar/java_grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .java_grammarParser import java_grammarParser
else:
    from java_grammarParser import java_grammarParser

# This class defines a complete generic visitor for a parse tree produced by java_grammarParser.

class java_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by java_grammarParser#program.
    def visitProgram(self, ctx:java_grammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#importDeclaration.
    def visitImportDeclaration(self, ctx:java_grammarParser.ImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx:java_grammarParser.PackageDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#structerDeclaration.
    def visitStructerDeclaration(self, ctx:java_grammarParser.StructerDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#classDeclaration.
    def visitClassDeclaration(self, ctx:java_grammarParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#classBody.
    def visitClassBody(self, ctx:java_grammarParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#superClass.
    def visitSuperClass(self, ctx:java_grammarParser.SuperClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#interfaces.
    def visitInterfaces(self, ctx:java_grammarParser.InterfacesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#classMemberDeclaration.
    def visitClassMemberDeclaration(self, ctx:java_grammarParser.ClassMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#constructor.
    def visitConstructor(self, ctx:java_grammarParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:java_grammarParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#enumBody.
    def visitEnumBody(self, ctx:java_grammarParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:java_grammarParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#interfaceBody.
    def visitInterfaceBody(self, ctx:java_grammarParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#interfaceMemberDeclaration.
    def visitInterfaceMemberDeclaration(self, ctx:java_grammarParser.InterfaceMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:java_grammarParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:java_grammarParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#throwedExeption.
    def visitThrowedExeption(self, ctx:java_grammarParser.ThrowedExeptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#formalParameters.
    def visitFormalParameters(self, ctx:java_grammarParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#formalParameter.
    def visitFormalParameter(self, ctx:java_grammarParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#methodBody.
    def visitMethodBody(self, ctx:java_grammarParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#block.
    def visitBlock(self, ctx:java_grammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:java_grammarParser.VariableDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#statement.
    def visitStatement(self, ctx:java_grammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#fullIfStatement.
    def visitFullIfStatement(self, ctx:java_grammarParser.FullIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#ifStatement.
    def visitIfStatement(self, ctx:java_grammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:java_grammarParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#elseStatement.
    def visitElseStatement(self, ctx:java_grammarParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#whileStatement.
    def visitWhileStatement(self, ctx:java_grammarParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:java_grammarParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#forStatement.
    def visitForStatement(self, ctx:java_grammarParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#forControl.
    def visitForControl(self, ctx:java_grammarParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#traditionalForControl.
    def visitTraditionalForControl(self, ctx:java_grammarParser.TraditionalForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#forInit.
    def visitForInit(self, ctx:java_grammarParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#forCondition.
    def visitForCondition(self, ctx:java_grammarParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#forUpdate.
    def visitForUpdate(self, ctx:java_grammarParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#enhancedForControl.
    def visitEnhancedForControl(self, ctx:java_grammarParser.EnhancedForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#switchStatement.
    def visitSwitchStatement(self, ctx:java_grammarParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#switchBlock.
    def visitSwitchBlock(self, ctx:java_grammarParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:java_grammarParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#switchLabel.
    def visitSwitchLabel(self, ctx:java_grammarParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#tryStatement.
    def visitTryStatement(self, ctx:java_grammarParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#catchClause.
    def visitCatchClause(self, ctx:java_grammarParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#catchFormalParameter.
    def visitCatchFormalParameter(self, ctx:java_grammarParser.CatchFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#finallyBlock.
    def visitFinallyBlock(self, ctx:java_grammarParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#returnStatement.
    def visitReturnStatement(self, ctx:java_grammarParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#breakStatement.
    def visitBreakStatement(self, ctx:java_grammarParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#continueStatement.
    def visitContinueStatement(self, ctx:java_grammarParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#throwStatement.
    def visitThrowStatement(self, ctx:java_grammarParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#expression.
    def visitExpression(self, ctx:java_grammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#logicalExpression.
    def visitLogicalExpression(self, ctx:java_grammarParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#logicalTerm.
    def visitLogicalTerm(self, ctx:java_grammarParser.LogicalTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#unaryLogicalExpression.
    def visitUnaryLogicalExpression(self, ctx:java_grammarParser.UnaryLogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#logicalOperator.
    def visitLogicalOperator(self, ctx:java_grammarParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:java_grammarParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#arithmeticTerm.
    def visitArithmeticTerm(self, ctx:java_grammarParser.ArithmeticTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#unaryArithmeticExpression.
    def visitUnaryArithmeticExpression(self, ctx:java_grammarParser.UnaryArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:java_grammarParser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:java_grammarParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#assignedValue.
    def visitAssignedValue(self, ctx:java_grammarParser.AssignedValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:java_grammarParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#literal.
    def visitLiteral(self, ctx:java_grammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#newInstance.
    def visitNewInstance(self, ctx:java_grammarParser.NewInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#incrementStatement.
    def visitIncrementStatement(self, ctx:java_grammarParser.IncrementStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#decrementStatement.
    def visitDecrementStatement(self, ctx:java_grammarParser.DecrementStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#functionCall.
    def visitFunctionCall(self, ctx:java_grammarParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#parameters.
    def visitParameters(self, ctx:java_grammarParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#parameter.
    def visitParameter(self, ctx:java_grammarParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#type.
    def visitType(self, ctx:java_grammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#dataType.
    def visitDataType(self, ctx:java_grammarParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#modifiers.
    def visitModifiers(self, ctx:java_grammarParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#modifier.
    def visitModifier(self, ctx:java_grammarParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#classModifiers.
    def visitClassModifiers(self, ctx:java_grammarParser.ClassModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#classModifier.
    def visitClassModifier(self, ctx:java_grammarParser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#dataStructerDeclaration.
    def visitDataStructerDeclaration(self, ctx:java_grammarParser.DataStructerDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#dataStructers.
    def visitDataStructers(self, ctx:java_grammarParser.DataStructersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#printStatement.
    def visitPrintStatement(self, ctx:java_grammarParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#inputStatement.
    def visitInputStatement(self, ctx:java_grammarParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#extendedIDwithThis.
    def visitExtendedIDwithThis(self, ctx:java_grammarParser.ExtendedIDwithThisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java_grammarParser#extendedID.
    def visitExtendedID(self, ctx:java_grammarParser.ExtendedIDContext):
        return self.visitChildren(ctx)



del java_grammarParser