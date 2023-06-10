from __future__ import annotations
from dataclasses import dataclass
from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor

@dataclass
class Letter:
    letter: str

@dataclass
class Application:
    left: Terme
    right: Terme

@dataclass
class Abstraction:
    var: str
    term: Terme

Terme = Letter | Application | Abstraction

class TreeVisitor(lcVisitor):
    # Visit a parse tree produced by lcParser#app.
    def visitApp(self, ctx):
        [leftTerm, rightTerm] = list(ctx.getChildren())
        return Application(self.visit(leftTerm), self.visit(rightTerm))

    # Visit a parse tree produced by lcParser#abs.
    def visitAbs(self, ctx):
        [lambd, vars, point, term] = list(ctx.getChildren())
        abs = self.visit(term)
        #Multiples variables
        for var in reversed(vars.getText()):
            abs = Abstraction(var, abs)
        return abs

    # Visit a parse tree produced by lcParser#letter.
    def visitLetter(self, ctx:lcParser.LetterContext):
        [letter] = list(ctx.getChildren())
        return Letter(letter.getText())

    # Visit a parse tree produced by lcParser#term.
    def visitTerm(self, ctx:lcParser.TermContext):
        [p1, term, p2] = list(ctx.getChildren())
        return self.visit(term)

def treeToStr(tree):
    match tree:
        case Application(left, right):
            return '(' + treeToStr(left) + treeToStr(right) + ')'
        case Abstraction(var, term):
            return '(λ' + var + '.' + treeToStr(term) + ')'
        case Letter(letter):
            return letter

def evalExpr(expr):
    match expr:
        case Application(left, right):
            match left:
                case Abstraction(var, absTerm):
                    [converted, absConverted, conversion] = alphaconversion(var, absTerm, right)
                    if converted:
                        reduction = 'α-conversió:\n' + alphaconversion
                        return True, Application(absConverted, subs), reduction
                    else:
                        reducedExpr = betareduction(var, absTerm, right)
                        reduction = 'β-reducció:\n' + treeToStr(expr) + ' → ' + treeToStr(reducedExpr)
                        return True, reducedExpr, reduction
                        
                            
                case _:
                    [reduced, redLeft, reduction] = evalExpr(left)
                    if (reduced):
                        app = Application(redLeft, right)
                        return True, app, reduction
                    else:
                        [reduced, redRight, reduction] = evalExpr(right)
                        app = Application(left, redRight)
                        return reduced, app, reduction
        case Abstraction(var, term):
            [reduced, redTerm, reduction] = evalExpr(term)
            abs = Abstraction(var, redTerm)
            return reduced, abs, reduction
        case Letter(letter):
            return False, Letter(letter), ''

def betareduction(var, absTerm, subs):
    match absTerm:
        case Application(left, right):
            [redLeft, reductionL] = betareduction(var, left, subs)
            [redRight, reductionR] = betareduction(var, right, subs)
            
            # if reductionL == 'beta' or reductionR == 'beta':
            #     reduction = 'beta'
            return  Application(redLeft, redRight)
        case Abstraction(absVar, term):
            if var != absVar:
                [redTerm, reduction] = betareduction(var, term, subs)
                return Abstraction(absVar, redTerm)
            else:
                return Abstraction(absVar, term)
        case Letter(letter):
            if letter == var:
                return subs
            else:
                return Letter(letter)

#Funció que aplica la alfa-conversió, retorna l'ABSTRACCIO amb la conversió aplicada
def alphaconversion(var, absTerm, rightTerm):
    abc = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

    BVabs, usedVarsAbs= boundVariables(Abstraction(var, absTerm))
    if BVabs.count(var) > 1:    #En l'abstraccio hi ha solapament de variables lligades
        freeNames = abc - usedVarsAbs
        oneName = freeNames.pop()
        renamedTerm, conversio = rename(absTerm, var, oneName, False)
        return True, Abstraction(var, renamedTerm), conversio
    else:
        FVright, usedVarsRTerm = freeVariables(rightTerm)

        freeNames = abc - (usedVarsAbs | usedVarsRTerm)
        conflictVars = FVright & set(BVabs)

        if conflictVars == set(): #Conjunt buit, no hi ha conflictes, retornem original
            return False, absTerm
        else: #Hi ha conflictes, resolem UN conflicte, canviant la primera variable de l'abstraccio que estigui en el conflicte
            oneConflict = conflictVars.pop()
            oneName = freeNames.pop()
            renamedAbs, conversio = rename(Abstraction(var, absTerm), oneConflict, oneName, False)
            return True, renamedAbs, conversio


#Funcio que retorna les variables lliures d'un terme, i les utilitzades (lligades o lliures)
def freeVariables(term):
    match term:
        case Application(left , right): 
            freeVarsLeft, varsUsedL = freeVariables(left)
            freeVarsRight, varsUsedR = freeVariables(right)
            return freeVarsLeft | freeVarsRight, varsUsedL | varsUsedR
        case Abstraction(var, term):
            freeVarsTerm, varsUsed = freeVariables(term)
            return freeVarsTerm - {var}, varsUsed | {var}
        case Letter(letter):
            return {letter}, {letter}

def boundVariables(term):
    match term:
        case Abstraction(var, absTerm):
            boundVarsTerm, varsUsed = boundVariables(absTerm)
            return [var] + boundVarsTerm, {var} | varsUsed 
        case Application(left, right):
            boundVarsLeft, varsUsedL = boundVariables(left)
            boundVarsRight, varsUsedR = boundVariables(right)
            return boundVarsLeft + boundVarsRight, varsUsedL | varsUsedR
        case Letter(letter):
            return [], {letter}

def rename(term, conflict, newName, found):
    match term:
        case Application(left, right):
            newLeft, conversioL = rename(left, conflict, newName, found)
            newRight, conversioR = rename(right, conflict, newName, found)
            conversio = None
            if conversioL != None and conversioR != None:
                conversio = treeToStr(term) + ' → ' + treeToStr(Application(newLeft, newRight))
            elif conversioL == None and conversioR != None:
                conversio = conversioR
            elif conversioL != None and conversioR == None:
                conversio = conversioL
            return Application(newLeft, newRight), conversio
        case Abstraction(var, term):
            if var == conflict and not found:
                newTerm, conversio = rename(term, conflict, newName, True)
                conversio = treeToStr(term) + ' → ' + treeToStr(newTerm)
                return Abstraction(newName, newTerm), conversio
            elif var == conflict and found:
                return Abstraction(var, term), None
            else:
                newTerm, conversio = rename(term, conflict, newName, found)
                return Abstraction(var, newTerm), conversio

        case Letter(letter):
            if found and letter == conflict:
                return Letter(newName), None
            else:
                return Letter(letter), None


while True:
    input_stream = InputStream(input('? '))
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()
    if parser.getNumberOfSyntaxErrors() == 0:
        #Visitor
        visitor = TreeVisitor()
        expression = visitor.visit(tree)
        print('Arbre: \n' + treeToStr(expression))
        #Evaluator
        maxReductions = 10 #Maximum limit of reductions 

        numReduc = 0
        reducedExpr = expression
        reduced = False
        while numReduc < maxReductions:
            [reduced, reducedExpr, reduction] = evalExpr(reducedExpr)
            if reduced:
                print(reduction)
                numReduc = numReduc + 1
            else:
                break
        #Result
        if reduced and numReduc >= maxReductions:
            print('Resultat:\n' + 'Nothing')
        else:
            print('Resultat:\n' + treeToStr(reducedExpr))

    else:
        print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        print(tree.toStringTree(recog=parser))