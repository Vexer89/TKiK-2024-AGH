grammar java_grammar;

// Reguły dla programu
program : (importDeclaration | packageDeclaration)* PUBLIC structerDeclaration+ ;

// Reguły dla importów
importDeclaration : IMPORT extendedID SEMICOLON ;
packageDeclaration : PACKAGE extendedID SEMICOLON ;

//Reguły dla klas, enum i interfejsów
structerDeclaration : classDeclaration
                    | interfaceDeclaration
                    | enumDeclaration;

//Klasa
classDeclaration : classModifiers? CLASS ID superClass? interfaces? classBody ;
classBody : LBRACE (classMemberDeclaration)* RBRACE ;
superClass : EXTENDS ID (COMMA ID)* ;
interfaces : IMPLEMENTS ID (COMMA ID)* ;

classMemberDeclaration : fieldDeclaration 
                       | methodDeclaration 
                       | classDeclaration 
                       | interfaceDeclaration
                       ;

//Enum
enumDeclaration : DEFAULT? ENUM ID enumBody ;
enumBody : LBRACE ID (COMMA ID)* SEMICOLON (classMemberDeclaration)* RBRACE;

//Interfejs
interfaceDeclaration : DEFAULT? INTERFACE ID interfaceBody;
interfaceBody : LBRACE (interfaceMemberDeclaration)* RBRACE;
interfaceMemberDeclaration : fieldDeclaration 
                           | methodDeclaration 
                           | interfaceDeclaration
                           ;

//Atrybuty
fieldDeclaration : modifiers? variableDeclarators SEMICOLON;

//Metody
methodDeclaration : modifiers? type ID LPAREN formalParameters? RPAREN throwedExeption? methodBody ;
throwedExeption : THROWS ID (COMMA ID)*;


formalParameters : formalParameter (COMMA formalParameter)* ;
formalParameter : type ID ;

methodBody : block ;
block : LBRACE blockStatement* RBRACE ;

blockStatement : statement SEMICOLON ;
variableDeclarators : type (ID (ASSIGN literal)?)+ ;

// Reguły dla instrukcji
statement : ifStatement
          | whileStatement
          | doWhileStatement
          | forStatement
          | switchStatement
          | tryStatement
          | returnStatement
          | breakStatement
          | continueStatement
          | throwStatement
          | expression
          | block
          | assignmentStatement
          | incrementStatement
          | decrementStatement
          | functionCall
          | printStatement
          | inputStatement
          ;
ifStatement : IF (logicalExpression | LPAREN LOGICAL_NOT? (extendedIDwithThis | literal) RPAREN) LBRACE statement RBRACE (ELSE statement)?;
whileStatement : WHILE (logicalExpression | LPAREN LOGICAL_NOT? (extendedIDwithThis | literal) RPAREN) LBRACE statement RBRACE ;
doWhileStatement : DO LBRACE statement RBRACE WHILE (logicalExpression | LPAREN LOGICAL_NOT? (extendedIDwithThis | literal) RPAREN);
forStatement : FOR LPAREN forControl RPAREN LBRACE statement RBRACE ;
forControl : enhancedForControl 
           | traditionalForControl 
           ;
traditionalForControl : forInit SEMICOLON logicalExpression SEMICOLON forUpdate ;
forInit : assignmentStatement
        | extendedIDwithThis
        ;
forUpdate : (arithmeticExpression | incrementStatement | decrementStatement) ;
enhancedForControl : type ID COLON extendedIDwithThis ;
switchStatement : SWITCH LPAREN extendedIDwithThis RPAREN switchBlock ;
switchBlock : LBRACE (switchBlockStatementGroup)* RBRACE ;
switchBlockStatementGroup : switchLabel+ block ;
switchLabel : CASE literal COLON | DEFAULT COLON ;
tryStatement : TRY block (catchClause+ finallyBlock? | finallyBlock) ;
catchClause : CATCH LPAREN catchFormalParameter RPAREN block ;
catchFormalParameter : type ID ;
finallyBlock : FINALLY block ;
returnStatement : RETURN (expression | extendedIDwithThis | literal)? SEMICOLON ;
breakStatement : BREAK SEMICOLON ;
continueStatement : CONTINUE SEMICOLON ;
throwStatement : THROW (ID | newInstance) SEMICOLON ;

//Reguły dla wyrażeń

expression : logicalExpression
           | arithmeticExpression
           ;

logicalExpression
    : logicalTerm
    | logicalExpression logicalOperator logicalTerm
    ;

logicalTerm
    : extendedIDwithThis
    | literal
    | unaryLogicalExpression
    | LPAREN logicalExpression RPAREN
    | LPAREN arithmeticExpression RPAREN
    | arithmeticExpression
    ;

unaryLogicalExpression
    : LOGICAL_NOT logicalTerm
    ;

logicalOperator
    : LOGICAL_OR
    | LOGICAL_AND
    | EQUAL
    | NOT_EQUAL
    | GREATER_THAN
    | LESS_THAN
    | LESS_THAN_OR_EQUAL
    | GREATER_THAN_OR_EQUAL
    ;

arithmeticExpression : arithmeticTerm
                    | arithmeticExpression arithmeticOperator arithmeticTerm;

arithmeticTerm : extendedIDwithThis
               | literal
               | unaryArithmeticExpression
               | LPAREN arithmeticExpression RPAREN
               ;

unaryArithmeticExpression: (ADD | SUB) arithmeticTerm;

arithmeticOperator: ADD
                 | SUB
                 | MUL
                 | DIV
                 | MOD
                 ;

//Przypisania
assignmentStatement : type? extendedIDwithThis assignmentOperator (extendedIDwithThis | literal | newInstance | expression | functionCall) ;
assignmentOperator : ASSIGN 
                   | ADD_ASSIGN 
                   | SUB_ASSIGN 
                   | MUL_ASSIGN 
                   | DIV_ASSIGN 
                   | MOD_ASSIGN
                   ;

//Dane
literal : INTEGER_NUMBER 
        | FLOAT_NUMBER 
        | STRING 
        | TRUE 
        | FALSE 
        | NULL 
        ;

//Tworzenie nowych obiektów
newInstance : NEW (ID | dataStructerDeclaration) LPAREN formalParameters RPAREN;

//Inkrementacja, dekrementacja
incrementStatement: extendedIDwithThis INCREMENT;
decrementStatement: extendedIDwithThis DECREMENT;

//Wywołanie metody
functionCall: extendedIDwithThis LPAREN extendedIDwithThis? (COMMA extendedIDwithThis)* RPAREN;

//Reguły dla typów danych
type : dataType 
     | VOID 
     | dataStructerDeclaration
     ;

dataType : INT | FLOAT | DOUBLE | LONG | SHORT | BYTE | CHAR | BOOLEAN | STRING;

//Modyfikatory
modifiers : modifier+ ;
modifier : PUBLIC 
         | PRIVATE 
         | PROTECTED
         | STATIC 
         | FINAL 
         | ABSTRACT 
         | DEFAULT
         ;
classModifiers : classModifier+ ;
classModifier : ABSTRACT
              | DEFAULT
              | FINAL
              ;

//Struktury danych
dataStructerDeclaration: dataStructers LESS_THAN (dataType | ID) GREATER_THAN ID
;

dataStructers : ARRAYLIST
              | LINKEDLIST
              | HASHSET
              | HASHMAP
              ;


//Obsługa lini komend
printStatement
    : (PRINT | PRINTLN) LPAREN expression RPAREN SEMICOLON
    ;

inputStatement
    : type ID ASSIGN NEW SCANNER LPAREN expression RPAREN DOT NEXT LPAREN RPAREN SEMICOLON
    ;

//Identyfikatory
extendedIDwithThis : THIS | ((THIS COMMA)? extendedID);

extendedID : ID (COMMA ID)* ;


//Tokens

//Data Structers
ARRAYLIST : 'ArrayList';
LINKEDLIST : 'LinkedList';
HASHSET : 'HashSet';
HASHMAP : 'HashMap';


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
THROWS : 'throws';

PRINT : 'System.out.print';
PRINTLN : 'System.out.println';
SCANNER : 'Scanner'; 
NEXT : 'next'; 

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
STRING : 'String';



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

STRING_TEXT
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