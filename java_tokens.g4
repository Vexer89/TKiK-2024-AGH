lexer grammar java_tokens;

//Tokens

//KeyWords
If : 'if';
Else : 'else';

Switch : 'switch';
Case : 'case';

While : 'while';
For : 'for';
Break : 'break';
Continue : 'continue';
Do : 'do';

Class : 'class';
Enum : 'enum';

Public : 'public';
Private : 'private';
Protected : 'protected';
Static : 'static';
Final : 'final';
Abstract : 'abstract';
Default : 'default';
Extends : 'extends';
Implements : 'implements';
Volatile : 'volataile';
Throws : 'throws';


True : 'true';
False : 'false';
Null : 'null';

Try : 'try';
Catch : 'catch';
Finally : 'finally';

New : 'new';
This : 'this';

Return : 'return';

Assert : 'assert';

Import : 'import';
Package : 'package';

Void : 'void';

// Operatory arytmetyczne
ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
MOD : '%' ;
// Nawiasy
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LSQUARE : '[' ;
RSQUARE : ']' ;
// Operatory relacyjne
EQUAL : '==' ;
NOT_EQUAL : '!=' ;
GREATER_THAN : '>' ;
LESS_THAN : '<' ;
GREATER_THAN_OR_EQUAL : '>=' ;
LESS_THAN_OR_EQUAL : '<=' ;
// Operatory logiczne
LOGICAL_AND : '&&' ;
LOGICAL_OR : '||' ;
LOGICAL_NOT : '!' ;
// Operatory inkrementacji/dekrementacji
INCREMENT : '++' ;
DECREMENT : '--' ;
// Operatory przypisania
ASSIGN : '=' ;
ADD_ASSIGN : '+=' ;
SUB_ASSIGN : '-=' ;
MUL_ASSIGN : '*=' ;
DIV_ASSIGN : '/=' ;
MOD_ASSIGN : '%=' ;
// Inne
COLON : ':' ;
SEMICOLON : ';' ;
DOT : '.' ;
TERNARY : '?' ;
THE_DOUBLE_COLON : '::' ;

ID:
[a-zA-Z_$][a-zA-Z_$0-9]*;

INTEGER_NUMBER:
[0-9]+;

FLOATING_NUMBER:
[0-9]+.[0-9]+;

STRING_OF_CHARACTERS:
'"' ( ESC | ~["\\] )* '"';

fragment ESC:
'\\' .;

CHAR:
'\'' . '\'';

WHITESPACES
    : [ \t\r\n]+ -> skip
    ;

BLOCKCOMMENT
    :   '/*' .*? '*/' -> skip
    ;

SINGLELINECOMMENT
    :   '//' ~[\r\n]* -> skip
    ;