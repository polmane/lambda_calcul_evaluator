# Generated from lc.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#rootterm.
    def visitRootterm(self, ctx:lcParser.RoottermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#defmac.
    def visitDefmac(self, ctx:lcParser.DefmacContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#app.
    def visitApp(self, ctx:lcParser.AppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#abs.
    def visitAbs(self, ctx:lcParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#letter.
    def visitLetter(self, ctx:lcParser.LetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#term.
    def visitTerm(self, ctx:lcParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#conj.
    def visitConj(self, ctx:lcParser.ConjContext):
        return self.visitChildren(ctx)



del lcParser