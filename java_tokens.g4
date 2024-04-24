lexer grammar java_tokens;

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