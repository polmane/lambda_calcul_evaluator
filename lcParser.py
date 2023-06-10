# Generated from lc.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("$\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3\26\n\3\3\3\3\3\7\3\32\n\3")
        buf.write("\f\3\16\3\35\13\3\3\4\6\4 \n\4\r\4\16\4!\3\4\2\3\4\5\2")
        buf.write("\4\6\2\3\3\2\5\6\2$\2\b\3\2\2\2\4\25\3\2\2\2\6\37\3\2")
        buf.write("\2\2\b\t\5\4\3\2\t\3\3\2\2\2\n\13\b\3\1\2\13\f\7\3\2\2")
        buf.write("\f\r\5\4\3\2\r\16\7\4\2\2\16\26\3\2\2\2\17\20\t\2\2\2")
        buf.write("\20\21\5\6\4\2\21\22\7\7\2\2\22\23\5\4\3\4\23\26\3\2\2")
        buf.write("\2\24\26\7\b\2\2\25\n\3\2\2\2\25\17\3\2\2\2\25\24\3\2")
        buf.write("\2\2\26\33\3\2\2\2\27\30\f\5\2\2\30\32\5\4\3\6\31\27\3")
        buf.write("\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\5")
        buf.write("\3\2\2\2\35\33\3\2\2\2\36 \7\b\2\2\37\36\3\2\2\2 !\3\2")
        buf.write("\2\2!\37\3\2\2\2!\"\3\2\2\2\"\7\3\2\2\2\5\25\33!")
        return buf.getvalue()


class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\u03BB'", "'\\'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LLETRA", "WS" ]

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
    LLETRA=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = lcParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermeContext(ParserRuleContext):

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
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [lcParser.T__0]:
                localctx = lcParser.TermContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.match(lcParser.T__0)
                self.state = 10
                self.terme(0)
                self.state = 11
                self.match(lcParser.T__1)
                pass
            elif token in [lcParser.T__2, lcParser.T__3]:
                localctx = lcParser.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                _la = self._input.LA(1)
                if not(_la==lcParser.T__2 or _la==lcParser.T__3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 14
                self.conj()
                self.state = 15
                self.match(lcParser.T__4)
                self.state = 16
                self.terme(2)
                pass
            elif token in [lcParser.LLETRA]:
                localctx = lcParser.LetterContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(lcParser.LLETRA)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lcParser.AppContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 21
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 22
                    self.terme(4) 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ConjContext(ParserRuleContext):

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
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.match(lcParser.LLETRA)
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==lcParser.LLETRA):
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
                return self.precpred(self._ctx, 3)
         




