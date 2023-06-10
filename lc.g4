grammar lc;

root : terme
     ;

terme : '(' terme ')'                   # term
      | terme terme                     # app
      | ('λ'|'\\') conj '.' terme       # abs
      | LLETRA                          # letter
      ;

conj: LLETRA+ ;
LLETRA : [a-z] ;
WS : [ \t\n\r]+ -> skip ;