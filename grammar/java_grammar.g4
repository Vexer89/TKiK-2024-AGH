grammar java_grammar;

// Reguły dla programu
program : (importDeclaration | packageDeclaration)* PUBLIC structerDeclaration+ EOF?;

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
                       | enumDeclaration
                       | constructor
                       ;

constructor : (PUBLIC | PROTECTED | PRIVATE) ID LPAREN formalParameters? RPAREN methodBody;

//Enum
enumDeclaration : DEFAULT? ENUM ID enumBody ;
enumBody : LBRACE ID (COMMA ID)* RBRACE;

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
methodDeclaration : modifiers? ABSTRACT? type ID LPAREN formalParameters? RPAREN throwedExeption? methodBody ;
throwedExeption : THROWS ID (COMMA ID)*;


formalParameters : formalParameter (COMMA formalParameter)* ;
formalParameter : type ID ;

methodBody : block ;
block : LBRACE statement* RBRACE ;

variableDeclarators : type ID (ASSIGN literal)? ;

// Reguły dla instrukcji
statement : fullIfStatement
          | whileStatement
          | doWhileStatement
          | forStatement
          | switchStatement
          | tryStatement
          | returnStatement
          | breakStatement
          | continueStatement
          | throwStatement
          | expression SEMICOLON
          | block
          | assignmentStatement SEMICOLON
          | incrementStatement SEMICOLON
          | decrementStatement SEMICOLON
          | functionCall SEMICOLON
          | printStatement
          | inputStatement
          ;

fullIfStatement : ifStatement elseIfStatement* elseStatement? ;
ifStatement : IF (logicalExpression | LPAREN LOGICAL_NOT? (extendedIDwithThis | literal) RPAREN) LBRACE statement+ RBRACE;
elseIfStatement : ELSE IF (logicalExpression | LPAREN LOGICAL_NOT? (extendedIDwithThis | literal) RPAREN) LBRACE statement+ RBRACE;
elseStatement : ELSE LBRACE statement+ RBRACE;
whileStatement : WHILE (logicalExpression | LPAREN LOGICAL_NOT? (extendedIDwithThis | literal) RPAREN) LBRACE statement+ RBRACE ;
doWhileStatement : DO LBRACE statement+ RBRACE WHILE (logicalExpression | LPAREN LOGICAL_NOT? (extendedIDwithThis | literal) RPAREN) SEMICOLON;
forStatement : FOR LPAREN forControl RPAREN LBRACE statement+ RBRACE ;
forControl : enhancedForControl 
           | traditionalForControl 
           ;
traditionalForControl : forInit SEMICOLON forCondition SEMICOLON forUpdate ;
forInit : assignmentStatement
        | extendedIDwithThis
        ;
forCondition : logicalExpression;
forUpdate : (incrementStatement | decrementStatement) ;
enhancedForControl : type ID COLON extendedIDwithThis ;
switchStatement : SWITCH LPAREN extendedIDwithThis RPAREN switchBlock ;
switchBlock : LBRACE (switchBlockStatementGroup)+ RBRACE ;
switchBlockStatementGroup : switchLabel statement+ ;
switchLabel : CASE literal COLON | DEFAULT COLON ;
tryStatement : TRY block catchClause+ finallyBlock? ;
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
assignmentStatement : type? extendedIDwithThis assignmentOperator assignedValue ;
assignedValue : extendedIDwithThis | literal | newInstance | expression | functionCall;
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
        | STRING_TEXT
        | CHARACTER
        | TRUE 
        | FALSE 
        | NULL 
        ;

//Tworzenie nowych obiektów
newInstance : NEW (ID | dataStructerDeclaration) LPAREN parameters? RPAREN;

//Inkrementacja, dekrementacja
incrementStatement: extendedIDwithThis INCREMENT;
decrementStatement: extendedIDwithThis DECREMENT;

//Wywołanie metody
functionCall: extendedIDwithThis LPAREN parameters? RPAREN;

parameters : (parameter) (COMMA (parameter))* ;
parameter : extendedIDwithThis | literal;


//Reguły dla typów danych
type : dataType 
     | VOID 
     | dataStructerDeclaration
     | extendedID
     ;

dataType : INT | FLOAT | DOUBLE | LONG | SHORT | BYTE | CHAR | BOOLEAN | STRING;

//Modyfikatory
modifiers : modifier+ ;
modifier : PUBLIC 
         | PRIVATE 
         | PROTECTED
         | STATIC
         | DEFAULT
         ;
classModifiers : classModifier+ ;
classModifier : ABSTRACT
              | DEFAULT
              | PROTECTED
              | PRIVATE
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
    : (PRINT | PRINTLN) LPAREN (expression | literal) RPAREN SEMICOLON
    ;

inputStatement
    : type ID ASSIGN NEW SCANNER LPAREN (expression | literal) RPAREN DOT NEXT LPAREN RPAREN SEMICOLON
    ;

//Identyfikatory
extendedIDwithThis : THIS | ((THIS DOT)? extendedID);

extendedID : ID (DOT ID)* ;

//comments: comment+;

//comment: BLOCKCOMMENT
//       | SINGLELINECOMMENT;



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

//NEWLINE : '\r'? '\n';