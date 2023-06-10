# Generated from lc.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,4,8,42,8,8,11,8,
        12,8,43,1,9,1,9,1,10,4,10,49,8,10,11,10,12,10,50,1,10,1,10,0,0,11,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,5,1,0,97,
        122,2,0,65,90,128,255,3,0,48,57,65,90,128,255,5,0,9,10,13,13,32,
        32,65,90,97,122,3,0,9,10,13,13,32,32,55,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,
        25,1,0,0,0,5,27,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,33,1,0,0,0,
        13,35,1,0,0,0,15,37,1,0,0,0,17,39,1,0,0,0,19,45,1,0,0,0,21,48,1,
        0,0,0,23,24,5,8801,0,0,24,2,1,0,0,0,25,26,5,61,0,0,26,4,1,0,0,0,
        27,28,5,40,0,0,28,6,1,0,0,0,29,30,5,41,0,0,30,8,1,0,0,0,31,32,5,
        955,0,0,32,10,1,0,0,0,33,34,5,92,0,0,34,12,1,0,0,0,35,36,5,46,0,
        0,36,14,1,0,0,0,37,38,7,0,0,0,38,16,1,0,0,0,39,41,7,1,0,0,40,42,
        7,2,0,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,
        44,18,1,0,0,0,45,46,8,3,0,0,46,20,1,0,0,0,47,49,7,4,0,0,48,47,1,
        0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,
        53,6,10,0,0,53,22,1,0,0,0,3,0,43,50,1,6,0,0
    ]

class lcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    LLETRA = 8
    MACRO = 9
    INMACRO = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\u2261'", "'='", "'('", "')'", "'\\u03BB'", "'\\'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "LLETRA", "MACRO", "INMACRO", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "LLETRA", "MACRO", "INMACRO", "WS" ]

    grammarFileName = "lc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


