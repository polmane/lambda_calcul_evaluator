# Generated from lc.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,42,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,3,0,11,8,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,1,1,1,1,
        1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,2,4,2,38,8,2,11,2,12,2,39,
        1,2,0,1,2,3,0,2,4,0,3,1,0,9,10,1,0,1,2,1,0,5,6,45,0,10,1,0,0,0,2,
        24,1,0,0,0,4,37,1,0,0,0,6,11,3,2,1,0,7,8,7,0,0,0,8,9,7,1,0,0,9,11,
        3,2,1,0,10,6,1,0,0,0,10,7,1,0,0,0,11,1,1,0,0,0,12,13,6,1,-1,0,13,
        25,5,9,0,0,14,15,5,3,0,0,15,16,3,2,1,0,16,17,5,4,0,0,17,25,1,0,0,
        0,18,19,7,2,0,0,19,20,3,4,2,0,20,21,5,7,0,0,21,22,3,2,1,2,22,25,
        1,0,0,0,23,25,5,8,0,0,24,12,1,0,0,0,24,14,1,0,0,0,24,18,1,0,0,0,
        24,23,1,0,0,0,25,33,1,0,0,0,26,27,10,5,0,0,27,28,5,10,0,0,28,32,
        3,2,1,6,29,30,10,3,0,0,30,32,3,2,1,4,31,26,1,0,0,0,31,29,1,0,0,0,
        32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,33,1,0,
        0,0,36,38,5,8,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,5,1,0,0,0,5,10,24,31,33,39
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u2261'", "'='", "'('", "')'", "'\\u03BB'", 
                     "'\\'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LLETRA", "MACRO", "INMACRO", "WS" ]

    RULE_root = 0
    RULE_terme = 1
    RULE_conj = 2

    ruleNames =  [ "root", "terme", "conj" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    LLETRA=8
    MACRO=9
    INMACRO=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_root

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TermrootContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermroot" ):
                return visitor.visitTermroot(self)
            else:
                return visitor.visitChildren(self)


    class DefmacContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)

        def MACRO(self):
            return self.getToken(lcParser.MACRO, 0)
        def INMACRO(self):
            return self.getToken(lcParser.INMACRO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefmac" ):
                return visitor.visitDefmac(self)
            else:
                return visitor.visitChildren(self)



    def root(self):

        localctx = lcParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = lcParser.TermrootContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.terme(0)
                pass

            elif la_ == 2:
                localctx = lcParser.DefmacContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 9
                self.terme(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_terme

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AppContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApp" ):
                return visitor.visitApp(self)
            else:
                return visitor.visitChildren(self)


    class AbsContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conj(self):
            return self.getTypedRuleContext(lcParser.ConjContext,0)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs" ):
                return visitor.visitAbs(self)
            else:
                return visitor.visitChildren(self)


    class LetterContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LLETRA(self):
            return self.getToken(lcParser.LLETRA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetter" ):
                return visitor.visitLetter(self)
            else:
                return visitor.visitChildren(self)


    class TermContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)


    class InfixContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)

        def INMACRO(self):
            return self.getToken(lcParser.INMACRO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfix" ):
                return visitor.visitInfix(self)
            else:
                return visitor.visitChildren(self)


    class MacContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MACRO(self):
            return self.getToken(lcParser.MACRO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMac" ):
                return visitor.visitMac(self)
            else:
                return visitor.visitChildren(self)



    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lcParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terme, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = lcParser.MacContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(lcParser.MACRO)
                pass
            elif token in [3]:
                localctx = lcParser.TermContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(lcParser.T__2)
                self.state = 15
                self.terme(0)
                self.state = 16
                self.match(lcParser.T__3)
                pass
            elif token in [5, 6]:
                localctx = lcParser.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 19
                self.conj()
                self.state = 20
                self.match(lcParser.T__6)
                self.state = 21
                self.terme(2)
                pass
            elif token in [8]:
                localctx = lcParser.LetterContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(lcParser.LLETRA)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 31
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.InfixContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        self.match(lcParser.INMACRO)
                        self.state = 28
                        self.terme(6)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.AppContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        self.terme(4)
                        pass

             
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLETRA(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.LLETRA)
            else:
                return self.getToken(lcParser.LLETRA, i)

        def getRuleIndex(self):
            return lcParser.RULE_conj

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConj" ):
                return visitor.visitConj(self)
            else:
                return visitor.visitChildren(self)




    def conj(self):

        localctx = lcParser.ConjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.match(lcParser.LLETRA)
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




