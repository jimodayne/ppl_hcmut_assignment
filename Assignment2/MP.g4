/*
 - Student name: Tran Duc Thinh
 - Student ID: 1652578
 */

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
boollit: TRUE|FALSE;

program
	: declaration+ EOF
	;

declaration
	: functionDeclaration
	| varDeclaration
	| procedureDeclaration
	;

varDeclaration: VAR varDeclarationList+ ;

varDeclarationList
	:
		identifierList COL primitiveType SEMI
		| identifierList COL ARRAY arrDeclaration SEMI
	;


functionDeclaration
	: FUNCTION funcName LB parameterList? RB COL returnType
	SEMI varDeclaration? compoundStatement
	;


procedureDeclaration
	: PROCEDURE procedureName LB parameterList? RB SEMI
	varDeclaration? compoundStatement
	;


funcName
	: identifier
	;

procedureName
	: identifier
	;

parameterList
	: parameterDeclaration (SEMI parameterDeclaration)*
	;

parameterDeclaration
	: identifierList COL returnType
	;

returnType
	: primitiveType
	| reComponentType
	;

reComponentType
	: ARRAY arrDeclaration
	;


componentType
	: ARRAY
	;

primitiveType
	: INTEGER
	| REAL
	| BOOLEAN
	| STRING
	;

identifierList
	: identifier (COM identifier)*
	;

arrDeclaration
	: LSB upArrSign? INTLIT DOD downArrSign? INTLIT RSB OF primitiveType
	;

upArrSign
	: SUBT
	;

downArrSign
	: SUBT
	;


string
	: STRINGLIT
	;

identifier
	: IDENT
	;

sign
	: ADDI
	| SUBT
	;

relationalOperator
	: LT
	| GT
	| LE
	| GE
	| EQUAL
	| NOT_EQUAL
	;

additiveOperator
   : ADDI
   | SUBT
   | OR
   ;

multiplicativeOperator
	: MULT
	| DIVI
	| DIV
   | MOD
   | AND
   ;


// statement

statements
	: statement+
	;

statement
	: nonSemiStateRule
	| semiStateRule
	;

semiStateRule
	: statementwithSemi SEMI
   ;

nonSemiStateRule
	: statementwithNoSemi
	;

statementwithSemi
	: assignmentStatement
	| breakStatement
	| continueStatement
	| returnStatement
	| callStatement
	;

statementwithNoSemi
	: ifStatement
	| forStatement
	| whileStatement
	| compoundStatement
	| withStatement
	;


lhs
	: indexExpression
	| identifier
	;


assignmentStatement
	: (lhs ASSIGN)+ expression
	;

ifStatement
	: IF expression THEN statement
	(ELSE statement)?
	;

whileStatement
	: WHILE expression DO statement
	;

forStatement
	: FOR identifier ASSIGN expression (TO|DOWNTO)
	expression DO statement
	;

breakStatement
	: BREAK
	;

continueStatement
	: CONTINUE
	;


returnStatement
	: RETURN expression?
	| RETURN
	;


withStatement
	: WITH varDeclarationList+ DO statement
	;

callStatement
	: identifier LB expressionList? RB
	;


compoundStatement
	: BEGIN statements? END
	;



// Expression

expression
	: calExpression
	| invocationExpression
	| indexExpression
	;


indexExpression
	: index1
	| index2
	| index3
	;

index1
	: identifier (LB expressionList? RB)? LSB expression RSB
	;

index2
	: LB expression RB LSB expression RSB
	;

index3
	: literals LSB expression RSB
	;


invocationExpression
	: identifier LB expressionList? RB
	;

expressionList
	: expression (COM expression)*
	;

/* expressionforIndex
	: expIn0
	;

expIn0
	: expIn0 (ADDI|SUBT) expIn1
	| expIn1
	;

expIn1
	: expIn1 (MULT|DIVI|DIV|MOD) expIn2
	| expIn2
	;

expIn2
	: SUBT expIn2
	| expIn3
	;

expIn3
	: expIn4 LSB expIn0 RSB
	| expIn4
	;

expIn4
	: LB expIn0 RB
	| INTLIT
	| identifier
	| indexExpression
	; */

calExpression
	: exp0
	;

/* exp0
	: exp0 (AND THEN | OR ELSE ) exp1
	| exp1
	; */


exp0
	: exp0 ( AND THEN | OR ELSE ) exp0 | exp1;

exp1
	: exp2 relationalOperator exp2
	| exp2
	;

exp2
	: exp2 additiveOperator exp3
	| exp3
	;

exp3
	: exp3 multiplicativeOperator exp4
	| exp4
	;

exp4
	: (NOT | SUBT) exp4
	| exp6
	;

/* exp5
	: exp6 LSB expression RSB
	| exp6
	; */

exp6
	: LB exp0 RB
	| literals
	| identifier
	| invocationExpression
	| indexExpression
	;


LSB: '[';
LB: '(' ;
RB: ')' ;
/* LP: '{';
RP: '}'; */
SEMI: ';';
RSB: ']';
DOD: '..';
COL: ':';
COM: ',';


fragment A
   : ('a' | 'A')
   ;


fragment B
   : ('b' | 'B')
   ;


fragment C
   : ('c' | 'C')
   ;


fragment D
   : ('d' | 'D')
	;


fragment E
   : ('e' | 'E')
   ;


fragment F
   : ('f' | 'F')
   ;


fragment G
   : ('g' | 'G')
   ;


fragment H
   : ('h' | 'H')
   ;


fragment I
   : ('i' | 'I')
   ;


fragment J
   : ('j' | 'J')
   ;


fragment K
   : ('k' | 'K')
   ;


fragment L
   : ('l' | 'L')
   ;


fragment M
   : ('m' | 'M')
   ;


fragment N
   : ('n' | 'N')
   ;


fragment O
   : ('o' | 'O')
   ;


fragment P
   : ('p' | 'P')
   ;


fragment Q
   : ('q' | 'Q')
   ;


fragment R
   : ('r' | 'R')
   ;


fragment S
   : ('s' | 'S')
   ;


fragment T
   : ('t' | 'T')
   ;


fragment U
   : ('u' | 'U')
   ;


fragment V
   : ('v' | 'V')
   ;


fragment W
   : ('w' | 'W')
   ;


fragment X
   : ('x' | 'X')
   ;


fragment Y
   : ('y' | 'Y')
   ;


fragment Z
   : ('z' | 'Z')
   ;



AND
	: A N D
	;


ARRAY
  : A R R A Y
  ;


BEGIN
  : B E G I N
  ;


BOOLEAN
  : B O O L E A N
  ;

BREAK
	: B R E A K
	;

CONTINUE
	: C O N T I N U E
	;

DOWNTO
	: D O W N T O
	;

DO
	: D O
	;

DIV
	: D I V
	;

END
	: E N D
	;

ELSE
	: E L S E
	;

FALSE
	: F A L S E
	;

FUNCTION
	: F U N C T I O N
	;

FOR
	: F O R
	;

INTEGER
	: I N T E G E R
	;

IF
	: I F
	;

MOD
	: M O D
	;

NOT
	: N O T
	;

OR
	: O R
	;

OF
	: O F
	;

PROCEDURE
  : P R O C E D U R E
  ;

REAL
	: R E A L
	;

RETURN
	: R E T U R N
	;

STRING
	: S T R I N G
	;

TO
	: T O
	;

TRUE
	: T R U E
	;

THEN
	: T H E N
	;

VAR
	: V A R
	;

WHILE
	: W H I L E
	;

WITH
	: W I T H
	;

// TOKEN SET


type_noarr: INTEGER|REAL|STRING|BOOLEAN;




// Keywords
/* fragment KW1: INTEGER|REAL|STRING|BOOLEAN|ARRAY;
fragment KW2: BREAK|CONTINUE|FOR|TO|DOWNTO|IF|THEN|ELSE|RETURN|WHILE|RETURN;
fragment KW3: BEGIN|END|FUNCTION|PROCEDURE|VAR|OF;
fragment KW4: NOT|OR|MOD|AND|DIV;
fragment KW5: TRUE|FALSE; */

/* KEYW: KW1 | KW2 | KW3 | KW4 | KW5 ; */



// Operators

ADDI
   : '+'
   ;


SUBT
   : '-'
   ;


MULT
   : '*'
   ;


DIVI
   : '/'
   ;


NOT_EQUAL
   : '<>'
   ;

EQUAL
   : '='
   ;

LT
   : '<'
   ;

LE
   : '<='
   ;


GE
   : '>='
   ;


GT
   : '>'
   ;

ASSIGN
	: ':='
	;

// Separators

SEPA: LB|RB|SEMI|LSB|RSB|DOD|COL|COM;



// Literals

literals: INTLIT|REALLIT|boollit|STRINGLIT;


// Identifiers:

IDENT: [a-zA-Z_][A-Za-z0-9_]* ;

INTLIT: Digit;

REALLIT :  (Digit '.' Digit ExponentPart?
         | Digit '.' Digit?
         | Digit '.'? ExponentPart
         | Digit? '.' Digit ExponentPart?);


STRINGLIT: '"' ('\\' ([tbfrn]  | '\'' | '"' | '\\' )
				| ~('\b' | '\f' | '\r' | '\n' | '\t' | '\'' | '"' | '\\'))* '"'
				{self.text = self.text[1:-1]} ;


fragment Digit: [0-9]+;

fragment ExponentPart: [eE][-]? Digit;

// Comment

/* : (COMMENT_1|COMMENT_2|COMMENT_3); */


 COMMENT_1
 	: '(*' .*? '*)'  -> skip
	;

 COMMENT_2
 	: '{' .*? '}' -> skip
	;

 COMMENT_3
 	: '//' ~[\r\n]*  -> skip
	;

WS
	: [ \t\r\n]+ -> skip // skip spaces, tabs, newlines
	;



ILLEGAL_ESCAPE: '"' (~[\\"'\n\t\r\f] | '\\' [ntfrb\\'"])* '\\' ~[ntrbf'"\\]
						{raise IllegalEscape(self.text[1:])} ;

UNCLOSE_STRING
	: '"' ('\\' ([tbfrn] | '\'' | '"' | '\\' )
	| ~('\b' | '\f' | '\r' | '\n' | '\t' | '\'' | '"' | '\\'))*
	{raise UncloseString(self.text[1:])}
	;

ERROR_CHAR: . {raise ErrorToken(self.text)};
 // error token - find exception in file lexererr.py
