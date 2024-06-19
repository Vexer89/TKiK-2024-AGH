# Generated from grammar/java_grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .java_grammarParser import java_grammarParser
else:
    from java_grammarParser import java_grammarParser

# This class defines a complete listener for a parse tree produced by java_grammarParser.
class java_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by java_grammarParser#program.
    def enterProgram(self, ctx:java_grammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by java_grammarParser#program.
    def exitProgram(self, ctx:java_grammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by java_grammarParser#importDeclaration.
    def enterImportDeclaration(self, ctx:java_grammarParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#importDeclaration.
    def exitImportDeclaration(self, ctx:java_grammarParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:java_grammarParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:java_grammarParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#structerDeclaration.
    def enterStructerDeclaration(self, ctx:java_grammarParser.StructerDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#structerDeclaration.
    def exitStructerDeclaration(self, ctx:java_grammarParser.StructerDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#classDeclaration.
    def enterClassDeclaration(self, ctx:java_grammarParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#classDeclaration.
    def exitClassDeclaration(self, ctx:java_grammarParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#classBody.
    def enterClassBody(self, ctx:java_grammarParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by java_grammarParser#classBody.
    def exitClassBody(self, ctx:java_grammarParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by java_grammarParser#superClass.
    def enterSuperClass(self, ctx:java_grammarParser.SuperClassContext):
        pass

    # Exit a parse tree produced by java_grammarParser#superClass.
    def exitSuperClass(self, ctx:java_grammarParser.SuperClassContext):
        pass


    # Enter a parse tree produced by java_grammarParser#interfaces.
    def enterInterfaces(self, ctx:java_grammarParser.InterfacesContext):
        pass

    # Exit a parse tree produced by java_grammarParser#interfaces.
    def exitInterfaces(self, ctx:java_grammarParser.InterfacesContext):
        pass


    # Enter a parse tree produced by java_grammarParser#classMemberDeclaration.
    def enterClassMemberDeclaration(self, ctx:java_grammarParser.ClassMemberDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#classMemberDeclaration.
    def exitClassMemberDeclaration(self, ctx:java_grammarParser.ClassMemberDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#constructor.
    def enterConstructor(self, ctx:java_grammarParser.ConstructorContext):
        pass

    # Exit a parse tree produced by java_grammarParser#constructor.
    def exitConstructor(self, ctx:java_grammarParser.ConstructorContext):
        pass


    # Enter a parse tree produced by java_grammarParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:java_grammarParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:java_grammarParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#enumBody.
    def enterEnumBody(self, ctx:java_grammarParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by java_grammarParser#enumBody.
    def exitEnumBody(self, ctx:java_grammarParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by java_grammarParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:java_grammarParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:java_grammarParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#interfaceBody.
    def enterInterfaceBody(self, ctx:java_grammarParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by java_grammarParser#interfaceBody.
    def exitInterfaceBody(self, ctx:java_grammarParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by java_grammarParser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:java_grammarParser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:java_grammarParser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:java_grammarParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:java_grammarParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:java_grammarParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:java_grammarParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#throwedExeption.
    def enterThrowedExeption(self, ctx:java_grammarParser.ThrowedExeptionContext):
        pass

    # Exit a parse tree produced by java_grammarParser#throwedExeption.
    def exitThrowedExeption(self, ctx:java_grammarParser.ThrowedExeptionContext):
        pass


    # Enter a parse tree produced by java_grammarParser#formalParameters.
    def enterFormalParameters(self, ctx:java_grammarParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by java_grammarParser#formalParameters.
    def exitFormalParameters(self, ctx:java_grammarParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by java_grammarParser#formalParameter.
    def enterFormalParameter(self, ctx:java_grammarParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by java_grammarParser#formalParameter.
    def exitFormalParameter(self, ctx:java_grammarParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by java_grammarParser#methodBody.
    def enterMethodBody(self, ctx:java_grammarParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by java_grammarParser#methodBody.
    def exitMethodBody(self, ctx:java_grammarParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by java_grammarParser#block.
    def enterBlock(self, ctx:java_grammarParser.BlockContext):
        pass

    # Exit a parse tree produced by java_grammarParser#block.
    def exitBlock(self, ctx:java_grammarParser.BlockContext):
        pass


    # Enter a parse tree produced by java_grammarParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:java_grammarParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by java_grammarParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:java_grammarParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by java_grammarParser#statement.
    def enterStatement(self, ctx:java_grammarParser.StatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#statement.
    def exitStatement(self, ctx:java_grammarParser.StatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#fullIfStatement.
    def enterFullIfStatement(self, ctx:java_grammarParser.FullIfStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#fullIfStatement.
    def exitFullIfStatement(self, ctx:java_grammarParser.FullIfStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#ifStatement.
    def enterIfStatement(self, ctx:java_grammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#ifStatement.
    def exitIfStatement(self, ctx:java_grammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:java_grammarParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:java_grammarParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#elseStatement.
    def enterElseStatement(self, ctx:java_grammarParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#elseStatement.
    def exitElseStatement(self, ctx:java_grammarParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#whileStatement.
    def enterWhileStatement(self, ctx:java_grammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#whileStatement.
    def exitWhileStatement(self, ctx:java_grammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:java_grammarParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:java_grammarParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#forStatement.
    def enterForStatement(self, ctx:java_grammarParser.ForStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#forStatement.
    def exitForStatement(self, ctx:java_grammarParser.ForStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#forControl.
    def enterForControl(self, ctx:java_grammarParser.ForControlContext):
        pass

    # Exit a parse tree produced by java_grammarParser#forControl.
    def exitForControl(self, ctx:java_grammarParser.ForControlContext):
        pass


    # Enter a parse tree produced by java_grammarParser#traditionalForControl.
    def enterTraditionalForControl(self, ctx:java_grammarParser.TraditionalForControlContext):
        pass

    # Exit a parse tree produced by java_grammarParser#traditionalForControl.
    def exitTraditionalForControl(self, ctx:java_grammarParser.TraditionalForControlContext):
        pass


    # Enter a parse tree produced by java_grammarParser#forInit.
    def enterForInit(self, ctx:java_grammarParser.ForInitContext):
        pass

    # Exit a parse tree produced by java_grammarParser#forInit.
    def exitForInit(self, ctx:java_grammarParser.ForInitContext):
        pass


    # Enter a parse tree produced by java_grammarParser#forCondition.
    def enterForCondition(self, ctx:java_grammarParser.ForConditionContext):
        pass

    # Exit a parse tree produced by java_grammarParser#forCondition.
    def exitForCondition(self, ctx:java_grammarParser.ForConditionContext):
        pass


    # Enter a parse tree produced by java_grammarParser#forUpdate.
    def enterForUpdate(self, ctx:java_grammarParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by java_grammarParser#forUpdate.
    def exitForUpdate(self, ctx:java_grammarParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by java_grammarParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:java_grammarParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by java_grammarParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:java_grammarParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by java_grammarParser#switchStatement.
    def enterSwitchStatement(self, ctx:java_grammarParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#switchStatement.
    def exitSwitchStatement(self, ctx:java_grammarParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#switchBlock.
    def enterSwitchBlock(self, ctx:java_grammarParser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by java_grammarParser#switchBlock.
    def exitSwitchBlock(self, ctx:java_grammarParser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by java_grammarParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:java_grammarParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by java_grammarParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:java_grammarParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by java_grammarParser#switchLabel.
    def enterSwitchLabel(self, ctx:java_grammarParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by java_grammarParser#switchLabel.
    def exitSwitchLabel(self, ctx:java_grammarParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by java_grammarParser#tryStatement.
    def enterTryStatement(self, ctx:java_grammarParser.TryStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#tryStatement.
    def exitTryStatement(self, ctx:java_grammarParser.TryStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#catchClause.
    def enterCatchClause(self, ctx:java_grammarParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by java_grammarParser#catchClause.
    def exitCatchClause(self, ctx:java_grammarParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by java_grammarParser#catchFormalParameter.
    def enterCatchFormalParameter(self, ctx:java_grammarParser.CatchFormalParameterContext):
        pass

    # Exit a parse tree produced by java_grammarParser#catchFormalParameter.
    def exitCatchFormalParameter(self, ctx:java_grammarParser.CatchFormalParameterContext):
        pass


    # Enter a parse tree produced by java_grammarParser#finallyBlock.
    def enterFinallyBlock(self, ctx:java_grammarParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by java_grammarParser#finallyBlock.
    def exitFinallyBlock(self, ctx:java_grammarParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by java_grammarParser#returnStatement.
    def enterReturnStatement(self, ctx:java_grammarParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#returnStatement.
    def exitReturnStatement(self, ctx:java_grammarParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#breakStatement.
    def enterBreakStatement(self, ctx:java_grammarParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#breakStatement.
    def exitBreakStatement(self, ctx:java_grammarParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#continueStatement.
    def enterContinueStatement(self, ctx:java_grammarParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#continueStatement.
    def exitContinueStatement(self, ctx:java_grammarParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#throwStatement.
    def enterThrowStatement(self, ctx:java_grammarParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#throwStatement.
    def exitThrowStatement(self, ctx:java_grammarParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#expression.
    def enterExpression(self, ctx:java_grammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by java_grammarParser#expression.
    def exitExpression(self, ctx:java_grammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by java_grammarParser#logicalExpression.
    def enterLogicalExpression(self, ctx:java_grammarParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by java_grammarParser#logicalExpression.
    def exitLogicalExpression(self, ctx:java_grammarParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by java_grammarParser#logicalTerm.
    def enterLogicalTerm(self, ctx:java_grammarParser.LogicalTermContext):
        pass

    # Exit a parse tree produced by java_grammarParser#logicalTerm.
    def exitLogicalTerm(self, ctx:java_grammarParser.LogicalTermContext):
        pass


    # Enter a parse tree produced by java_grammarParser#unaryLogicalExpression.
    def enterUnaryLogicalExpression(self, ctx:java_grammarParser.UnaryLogicalExpressionContext):
        pass

    # Exit a parse tree produced by java_grammarParser#unaryLogicalExpression.
    def exitUnaryLogicalExpression(self, ctx:java_grammarParser.UnaryLogicalExpressionContext):
        pass


    # Enter a parse tree produced by java_grammarParser#logicalOperator.
    def enterLogicalOperator(self, ctx:java_grammarParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by java_grammarParser#logicalOperator.
    def exitLogicalOperator(self, ctx:java_grammarParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by java_grammarParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:java_grammarParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by java_grammarParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:java_grammarParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by java_grammarParser#arithmeticTerm.
    def enterArithmeticTerm(self, ctx:java_grammarParser.ArithmeticTermContext):
        pass

    # Exit a parse tree produced by java_grammarParser#arithmeticTerm.
    def exitArithmeticTerm(self, ctx:java_grammarParser.ArithmeticTermContext):
        pass


    # Enter a parse tree produced by java_grammarParser#unaryArithmeticExpression.
    def enterUnaryArithmeticExpression(self, ctx:java_grammarParser.UnaryArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by java_grammarParser#unaryArithmeticExpression.
    def exitUnaryArithmeticExpression(self, ctx:java_grammarParser.UnaryArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by java_grammarParser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:java_grammarParser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by java_grammarParser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:java_grammarParser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by java_grammarParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:java_grammarParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:java_grammarParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#assignedValue.
    def enterAssignedValue(self, ctx:java_grammarParser.AssignedValueContext):
        pass

    # Exit a parse tree produced by java_grammarParser#assignedValue.
    def exitAssignedValue(self, ctx:java_grammarParser.AssignedValueContext):
        pass


    # Enter a parse tree produced by java_grammarParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:java_grammarParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by java_grammarParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:java_grammarParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by java_grammarParser#literal.
    def enterLiteral(self, ctx:java_grammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by java_grammarParser#literal.
    def exitLiteral(self, ctx:java_grammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by java_grammarParser#newInstance.
    def enterNewInstance(self, ctx:java_grammarParser.NewInstanceContext):
        pass

    # Exit a parse tree produced by java_grammarParser#newInstance.
    def exitNewInstance(self, ctx:java_grammarParser.NewInstanceContext):
        pass


    # Enter a parse tree produced by java_grammarParser#incrementStatement.
    def enterIncrementStatement(self, ctx:java_grammarParser.IncrementStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#incrementStatement.
    def exitIncrementStatement(self, ctx:java_grammarParser.IncrementStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#decrementStatement.
    def enterDecrementStatement(self, ctx:java_grammarParser.DecrementStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#decrementStatement.
    def exitDecrementStatement(self, ctx:java_grammarParser.DecrementStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#functionCall.
    def enterFunctionCall(self, ctx:java_grammarParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by java_grammarParser#functionCall.
    def exitFunctionCall(self, ctx:java_grammarParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by java_grammarParser#parameters.
    def enterParameters(self, ctx:java_grammarParser.ParametersContext):
        pass

    # Exit a parse tree produced by java_grammarParser#parameters.
    def exitParameters(self, ctx:java_grammarParser.ParametersContext):
        pass


    # Enter a parse tree produced by java_grammarParser#parameter.
    def enterParameter(self, ctx:java_grammarParser.ParameterContext):
        pass

    # Exit a parse tree produced by java_grammarParser#parameter.
    def exitParameter(self, ctx:java_grammarParser.ParameterContext):
        pass


    # Enter a parse tree produced by java_grammarParser#type.
    def enterType(self, ctx:java_grammarParser.TypeContext):
        pass

    # Exit a parse tree produced by java_grammarParser#type.
    def exitType(self, ctx:java_grammarParser.TypeContext):
        pass


    # Enter a parse tree produced by java_grammarParser#dataType.
    def enterDataType(self, ctx:java_grammarParser.DataTypeContext):
        pass

    # Exit a parse tree produced by java_grammarParser#dataType.
    def exitDataType(self, ctx:java_grammarParser.DataTypeContext):
        pass


    # Enter a parse tree produced by java_grammarParser#modifiers.
    def enterModifiers(self, ctx:java_grammarParser.ModifiersContext):
        pass

    # Exit a parse tree produced by java_grammarParser#modifiers.
    def exitModifiers(self, ctx:java_grammarParser.ModifiersContext):
        pass


    # Enter a parse tree produced by java_grammarParser#modifier.
    def enterModifier(self, ctx:java_grammarParser.ModifierContext):
        pass

    # Exit a parse tree produced by java_grammarParser#modifier.
    def exitModifier(self, ctx:java_grammarParser.ModifierContext):
        pass


    # Enter a parse tree produced by java_grammarParser#classModifiers.
    def enterClassModifiers(self, ctx:java_grammarParser.ClassModifiersContext):
        pass

    # Exit a parse tree produced by java_grammarParser#classModifiers.
    def exitClassModifiers(self, ctx:java_grammarParser.ClassModifiersContext):
        pass


    # Enter a parse tree produced by java_grammarParser#classModifier.
    def enterClassModifier(self, ctx:java_grammarParser.ClassModifierContext):
        pass

    # Exit a parse tree produced by java_grammarParser#classModifier.
    def exitClassModifier(self, ctx:java_grammarParser.ClassModifierContext):
        pass


    # Enter a parse tree produced by java_grammarParser#dataStructerDeclaration.
    def enterDataStructerDeclaration(self, ctx:java_grammarParser.DataStructerDeclarationContext):
        pass

    # Exit a parse tree produced by java_grammarParser#dataStructerDeclaration.
    def exitDataStructerDeclaration(self, ctx:java_grammarParser.DataStructerDeclarationContext):
        pass


    # Enter a parse tree produced by java_grammarParser#dataStructers.
    def enterDataStructers(self, ctx:java_grammarParser.DataStructersContext):
        pass

    # Exit a parse tree produced by java_grammarParser#dataStructers.
    def exitDataStructers(self, ctx:java_grammarParser.DataStructersContext):
        pass


    # Enter a parse tree produced by java_grammarParser#printStatement.
    def enterPrintStatement(self, ctx:java_grammarParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#printStatement.
    def exitPrintStatement(self, ctx:java_grammarParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#inputStatement.
    def enterInputStatement(self, ctx:java_grammarParser.InputStatementContext):
        pass

    # Exit a parse tree produced by java_grammarParser#inputStatement.
    def exitInputStatement(self, ctx:java_grammarParser.InputStatementContext):
        pass


    # Enter a parse tree produced by java_grammarParser#extendedIDwithThis.
    def enterExtendedIDwithThis(self, ctx:java_grammarParser.ExtendedIDwithThisContext):
        pass

    # Exit a parse tree produced by java_grammarParser#extendedIDwithThis.
    def exitExtendedIDwithThis(self, ctx:java_grammarParser.ExtendedIDwithThisContext):
        pass


    # Enter a parse tree produced by java_grammarParser#extendedID.
    def enterExtendedID(self, ctx:java_grammarParser.ExtendedIDContext):
        pass

    # Exit a parse tree produced by java_grammarParser#extendedID.
    def exitExtendedID(self, ctx:java_grammarParser.ExtendedIDContext):
        pass



del java_grammarParser