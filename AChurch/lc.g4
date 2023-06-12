grammar lc;

root : terme                            # termroot
    | (MACRO|INMACRO) ('≡'|'=') terme   # defmac
    ;

terme : MACRO                           # mac
    | terme INMACRO terme               # infix
    | '(' terme ')'                     # term
    | terme terme                       # app
    | ('λ'|'\\') conj '.' terme         # abs
    | LLETRA                            # letter
    ;

conj: LLETRA+ ;
LLETRA : [a-z] ;
MACRO : [A-Z\u0080-\u00FF][0-9A-Z\u0080-\u00FF]+ ;
INMACRO : ~[a-zA-Z \t\r\n] ;
WS : [ \t\n\r]+ -> skip ;