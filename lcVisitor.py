# Generated from lc.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx:lcParser.RootContext):
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