grammar java_grammar;

// Reguły dla programu
program : (importDeclaration | packageDeclaration)* PUBLIC structerDeclaration+ ;

// Reguły dla importów
importDeclaration : IMPORT qualifiedName SEMICOLON ;
packageDeclaration : PACKAGE qualifiedName SEMICOLON ;
qualifiedName : ID (DOT ID)* ;

//Reguły dla klasy i interfejsu
structerDeclaration : classDeclaration
                    | interfaceDeclaration
                    | enumDeclaration;

classDeclaration : classModifiers? CLASS ID superClass? interfaces? classBody ;
classBody : LBRACE (classMemberDeclaration)* RBRACE ;
superClass : EXTENDS ID (COMMA ID)* ;
interfaces : IMPLEMENTS ID (COMMA ID)* ;

classMemberDeclaration : fieldDeclaration 
                       | methodDeclaration 
                       | classDeclaration 
                       | interfaceDeclaration
                       ;
methodDeclaration : modifiers? type ID LPAREN formalParameters? RPAREN throwedExeption? methodBody ;
throwedExeption : THROWS ID (COMMA ID)*;

fieldDeclaration : modifiers? type variableDeclarators SEMICOLON;

enumDeclaration : DEFAULT? ENUM ID enumBody ;
enumBody : LBRACE ID (COMMA ID)* SEMICOLON (classMemberDeclaration)* RBRACE;

interfaceDeclaration : DEFAULT? INTERFACE ID interfaceBody;
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
variableDeclarators : type? variableDeclarator (COMMA variableDeclarator)* ;
variableDeclarator : type? ID (ASSIGN variableInitializer)? ;
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
          | assignmentStatement
          | incrementStatement
          | decrementStatement
          | functionCall
          ;
expressionStatement : expression SEMICOLON ;
ifStatement : IF (logicalExpression | LPAREN LOGICAL_NOT? (ID | literal) RPAREN) LBRACE statement RBRACE (ELSE statement)?;
whileStatement : WHILE (logicalExpression | LPAREN LOGICAL_NOT? (ID | literal) RPAREN) LBRACE statement RBRACE ;
forStatement : FOR LPAREN forControl RPAREN LBRACE statement RBRACE ;
forControl : enhancedForControl 
           | traditionalForControl 
           ;
traditionalForControl : forInit SEMICOLON expression SEMICOLON forUpdate ;
forInit : variableDeclarator 
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
throwStatement : THROW (ID | newInstance) SEMICOLON ;

//Reguły dla wyrażeń


expression : logicalExpression
           | aritmeticExpression
           ;

logicalExpression : LOGICAL_NOT? LPAREN (expression | ID | literal) (LOGICAL_OR
                                               | LOGICAL_AND
                                               | EQUAL
                                               | NOT_EQUAL
                                               | GREATER_THAN
                                               | LESS_THAN
                                               | LESS_THAN_OR_EQUAL
                                               | GREATER_THAN_OR_EQUAL) (expression | ID | literal) RPAREN;

aritmeticExpression : LPAREN (expression | ID | literal) (ADD
                                                        | SUB
                                                        | MUL
                                                        | DIV
                                                        | MOD) (expression | ID | literal) RPAREN;//fix?

assignmentStatement : type? ID assignmentOperator (ID | literal | newInstance | expression | functionCall) ;
assignmentOperator : ASSIGN 
                   | ADD_ASSIGN 
                   | SUB_ASSIGN 
                   | MUL_ASSIGN 
                   | DIV_ASSIGN 
                   | MOD_ASSIGN
                   ;

literal : INTEGER_NUMBER 
        | FLOAT_NUMBER 
        | STRING 
        | TRUE 
        | FALSE 
        | NULL 
        ;

newInstance : NEW ID LPAREN formalParameters RPAREN;

incrementStatement: ID INCREMENT;
decrementStatement: ID DECREMENT;
functionCall: ID LPAREN ID? (COMMA ID)* RPAREN;

//Reguły dla typów danych
type : dataType 
     | VOID 
     //| referenceType
     ;
//referenceType : NEW? type ID (LESS_THAN typeArguments GREATER_THAN)? (LSQUARE RSQUARE)* ;
//typeArguments : type (COMMA type)* ;
modifiers : modifier+ ;
modifier : PUBLIC 
         | PRIVATE 
         | PROTECTED
         | STATIC 
         | FINAL 
         | ABSTRACT 
         | DEFAULT 
         | VOLATAILE 
         ;
classModifiers : classModifier+ ;
classModifier : ABSTRACT
              | DEFAULT
              | FINAL
              ;
dataType : INT | FLOAT | DOUBLE | LONG | SHORT | BYTE | CHAR | BOOLEAN;

//Tokens

//KeyWords
IF : 'if';
ELSE : 'else';

SWITCH : 'switch';
CASE : 'case';

WHILE : 'while';
FOR : 'for';
BREAK : 'break';
CONTINUE : 'continue';
DO : 'do';

CLASS : 'class';
INTERFACE : 'interface';
ENUM : 'enum';

PUBLIC : 'public';
PRIVATE : 'private';
PROTECTED : 'protected';
STATIC : 'static';
FINAL : 'final';
ABSTRACT : 'abstract';
DEFAULT : 'default';
EXTENDS : 'extends';
IMPLEMENTS : 'implements';
VOLATAILE : 'volataile';
THROWS : 'throws';


TRUE : 'true';
FALSE : 'false';
NULL : 'null';

THROW: 'throw';
TRY : 'try';
CATCH : 'catch';
FINALLY : 'finally';

NEW : 'new';
THIS : 'this';

RETURN : 'return';

ASSERT : 'assert';

IMPORT : 'import';
PACKAGE : 'package';

// arithmetic operators
ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
MOD : '%' ;
// brackets
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LSQUARE : '[' ;
RSQUARE : ']' ;
// relational operators
EQUAL : '==' ;
NOT_EQUAL : '!=' ;
GREATER_THAN : '>' ;
LESS_THAN : '<' ;
GREATER_THAN_OR_EQUAL : '>=' ;
LESS_THAN_OR_EQUAL : '<=' ;
// logical operators
LOGICAL_AND : '&&' ;
LOGICAL_OR : '||' ;
LOGICAL_NOT : '!' ;
// incremantion/decramentation operators
INCREMENT : '++' ;
DECREMENT : '--' ;
// assignment operators
ASSIGN : '=' ;
ADD_ASSIGN : '+=' ;
SUB_ASSIGN : '-=' ;
MUL_ASSIGN : '*=' ;
DIV_ASSIGN : '/=' ;
MOD_ASSIGN : '%=' ;
// other
COLON : ':' ;
SEMICOLON : ';' ;
DOT : '.' ;
COMMA : ',' ;
TERNARY : '?' ;
THE_DOUBLE_COLON : '::' ;

//data types
VOID : 'void';
INT : 'int';
FLOAT : 'float';
DOUBLE : 'double';
LONG : 'long';
SHORT : 'short';
BYTE : 'byte';
CHAR : 'char';
BOOLEAN : 'boolean';

ID
    :   [a-zA-Z_][a-zA-Z_$0-9]*
    ;

fragment DIGIT
    :   [0-9]
    ;

INTEGER_NUMBER
    :   DIGIT+
    ;

FLOAT_NUMBER
    :   DIGIT+.DIGIT+
    ;

STRING
    :   '"' ( ESC | ~["\\] )* '"'
    ;

fragment ESC
    :   '\\' .
    ;

CHARACTER
    :   '\'' . '\''
    ;

WHITESPACES
    : [ \t\r\n]+ -> skip
    ;

BLOCKCOMMENT
    :   '/*' .*? '*/' -> skip
    ;

SINGLELINECOMMENT
    :   '//' ~[\r\n]* -> skip
    ;