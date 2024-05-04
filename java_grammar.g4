grammar JavaGrammar;

// Reguły dla programu
program : (importDeclaration | packageDeclaration)* (classDeclaration)+;

// Reguły dla importów
importDeclaration : IMPORT qualifiedName SEMICOLON ;
packageDeclaration : PACKAGE qualifiedName SEMICOLON ;
qualifiedName : ID (DOT ID)* ;

//Reguły dla klasy i interfejsu
classDeclaration : modifiers? CLASS ID superClass? interfaces? classBody ;
classBody : LBRACE (classMemberDeclaration)* LBRACE ;
superClass : EXTENDS ID (COMMA ID)* ;
interfaces : IMPREMENTS ID (COMMA ID)* ;

classMemberDeclaration : fieldDeclaration 
                       | methodDeclaration 
                       | classDeclaration 
                       | interfaceDeclaration
                       ;
methodDeclaration : modifiers? type ID LPAREN formalParameters? RPAREN methodBody ;
fieldDeclaration : modifiers? type variableDeclarators SEMICOLON;
interfaceDeclaration : modifiers? INTERFACE ID interfaceBody;
interfaceBody : LBRACE (interfaceMemberDeclaration)* RBRACE;
interfaceMemberDeclaration : fieldDeclaration 
                           | methodDeclaration 
                           | interfaceDeclaration
                           ;
formalParameters : formalParameter (COMMA formalParameter)* ;
formalParameter : type ID ;
methodBody : block ;
block : LBRACE blockStatement* RBRACE ;

blockStatement : type variableDeclarators SEMICOLON 
               | statement SEMICOLON 
               ;
variableDeclarators : variableDeclarator (COMMA variableDeclarator)* ;
variableDeclarator : ID (ASSIGN variableInitializer)? ;
variableInitializer : literal ;

// Reguły dla instrukcji
statement : ifStatement
          | whileStatement
          | forStatement
          | switchStatement
          | tryStatement
          | returnStatement
          | breakStatement
          | continueStatement
          | throwStatement
          | expressionStatement
          | block
          ;
expressionStatement : expression SEMICOLON ;
ifStatement : IF LPAREN expression RPAREN statement (ELSE statement)?;
whileStatement : WHILE LPAREN expression RPAREN statement ;
forStatement : FOR LPAREN forControl RPAREN statement ;
forControl : enhancedForControl 
           | traditionalForControl 
           ;
traditionalForControl : forInit SEMICOLON expression SEMICOLON forUpdate ;
forInit : variableDeclaration 
        | expression 
        ;
forUpdate : expression ;
enhancedForControl : type ID COLON expression ;
switchStatement : SWITCH LPAREN expression RPAREN switchBlock ;
switchBlock : LBRACE (switchBlockStatementGroup)* RBRACE ;
switchBlockStatementGroup : switchLabel+ block ;
switchLabel : CASE expression COLON | DEFAULT COLON ;
tryStatement : TRY block (catchClause+ finallyBlock? | finallyBlock) ;
catchClause : CATCH LPAREN catchFormalParameter RPAREN block ;
catchFormalParameter : type ID ;
finallyBlock : FINALLY block ;
returnStatement : RETURN expression? SEMICOLON ;
breakStatement : BREAK ID? SEMICOLON ;
continueStatement : CONTINUE ID? SEMICOLON ;
throwStatement : THROW expression SEMICOLON ;

//Reguły dla wyrażeń
expression : logicalOrExpression 
           | assignmentExpression
           ;
assignmentExpression : unaryExpression assignmentOperator expression ;
assignmentOperator : ASSIGN 
                   | ADD_ASSIGN 
                   | SUB_ASSIGN 
                   | MUL_ASSIGN 
                   | DIV_ASSIGN 
                   | MOD_ASSIGN
                   ;
logicalOrExpression : logicalAndExpression LOGICAL_OR logicalAndExpression ;
logicalAndExpression : equalityExpression LOGICAL_AND equalityExpression ;
equalityExpression : relationalExpression (EQUAL | NOT_EQUAL) relationalExpression ;
relationalExpression : additiveExpression (GREATER_THAN | LESS_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL) additiveExpression ;
additiveExpression : multiplicativeExpression (ADD | SUB) multiplicativeExpression ;
multiplicativeExpression : unaryExpression (MUL | DIV | MOD) unaryExpression ;
unaryExpression : primary 
                | (ADD | SUB | LOGICAL_NOT | THE_DOUBLE_COLON) unaryExpression 
                | primary INCREMENT 
                | primary DECREMENT
                ;
primary : literal 
        | ID 
        | LPAREN expression RPAREN 
        ;
literal : INTEGER_NUMBER 
        | FLOAT_NUMBER 
        | STRING 
        | TRUE 
        | FALSE 
        | NULL 
        ;

//Reguły dla typów danych
type : dataType 
     | VOID 
     | referenceType 
     ;
referenceType : NEW? ID (LESS_THAN typeArguments GREATER_THAN)? (LSQUARE RSQUARE)* ;
typeArguments : type (COMMA type)* ;
modifiers : modifier+ ;
modifier : PUBLIC 
         | PRIVATE 
         | PROTECTED
         | STATIC 
         | FINAL 
         | ABSTRACT 
         | DEFAULT 
         | EXTENDS 
         | IMPLEMENTS 
         | VOLATAILE 
         | THROWS 
         ;
dataType : NEW? (INT | FLOAT | DOUBLE | LONG | SHORT | BYTE | CHAR | BOOLEAN) ;
