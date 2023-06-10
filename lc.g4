grammar lc;

root : terme                          #rootterm
    | (NOMMAC|INFIX) ('≡'|'=') terme  #defmac
    ;

terme : '(' terme ')'                 # term
    | terme terme                     # app
    | ('λ'|'\\') conj '.' terme       # abs
    | LLETRA                          # letter
    ;

conj: LLETRA+ ;
LLETRA : [a-z] ;
NOMMAC : [A-Z\u0080-\u00FF][0-9A-Z\u0080-\u00FF]+ ;
INFIX : ~[a-zA-Z \t\r\n] ;
WS : [ \t\n\r]+ -> skip ;