lexer grammar java;

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