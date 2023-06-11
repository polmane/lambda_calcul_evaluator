######################### IMPORTS #########################
from __future__ import annotations
from dataclasses import dataclass
from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

######################### CLASSES i VARIABLES #########################

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

macrosDictionary = dict()

######################### VISITOR #########################

class TreeVisitor(lcVisitor):
    # Visit a parse tree produced by lcParser#defmac.
    def visitDefmac(self, ctx):
        [nameDef, equal, term] = list(ctx.getChildren())
        macrosDictionary[nameDef.getText()] = self.visit(term)
        return 'defMacro'

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
    def visitLetter(self, ctx):
        [letter] = list(ctx.getChildren())
        return Letter(letter.getText())

    # Visit a parse tree produced by lcParser#term.
    def visitTerm(self, ctx):
        [p1, term, p2] = list(ctx.getChildren())
        return self.visit(term)
    
    # Visit a parse tree produced by lcParser#infix.
    def visitInfix(self, ctx):
        [term1, infix, term2] = list(ctx.getChildren())
        infixTerm = macrosDictionary[infix.getText()]
        exprTerm1 = self.visit(term1)
        exprTerm2 = self.visit(term2)
        return Application(Application(infixTerm, exprTerm1), exprTerm2)

    # Visit a parse tree produced by lcParser#mac.
    def visitMac(self, ctx):
        [name] = list(ctx.getChildren())
        return macrosDictionary[name.getText()]
    
######################### PROGRAMA PYTHON #########################

# Concatena els les claus i valors d'un diccionari "macrosIn" en una única string
def macrosToStr(macrosIn):
    if not bool(macrosIn):
        return 'No hi ha macros definides'
    else:
        sequence = ''
        for name, term in macrosIn.items():
            sequence = sequence + name + ' ≡ ' + treeToStr(term) +'\n'
        return sequence

# Donat una expressió en forma de arbre (definit com a Terme a dalt), retorna un string amb la representació d'arbre parentitzat
def treeToStr(tree):
    match tree:
        case Application(left, right):
            return '(' + treeToStr(left) + treeToStr(right) + ')'
        case Abstraction(var, term):
            return '(λ' + var + '.' + treeToStr(term) + ')'
        case Letter(letter):
            return letter

# Avalua una expressió (Terme) i si pot aplica UNA transformació i retorna tres variables:
    # reduced: Boolea que indica si ha patit UNA transformació (beta-reduccio o alfa-conversió)
    # reducedExpr: L'expressió transformada/reduida si s'escau, sinó serà la mateixa que d'entrada
    # reduction: Un string que representaa la reducció aplicada
def evalExpr(expr):
    match expr:
        case Application(left, right):
            match left:
                case Abstraction(var, absTerm):
                    [converted, absConverted] = alphaconversion(var, absTerm, right)
                    if converted:
                        reduction = 'α-conversió:\n' + treeToStr(left) + ' → ' + treeToStr(absConverted)
                        return True, Application(absConverted, right), reduction
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

# Funció que retorna l'expressió amb la beta reducció aplicada
def betareduction(var, absTerm, subs):
    match absTerm:
        case Application(left, right):
            redLeft= betareduction(var, left, subs)
            redRight = betareduction(var, right, subs)
            return  Application(redLeft, redRight)
        case Abstraction(absVar, term):
            if var != absVar:
                redTerm= betareduction(var, term, subs)
                return Abstraction(absVar, redTerm)
            else:
                #Per si de cas, però l'alfa-conversio se n'hauria d'encarregar
                return Abstraction(absVar, term)
        case Letter(letter):
            if letter == var:
                return subs
            else:
                return Letter(letter)

#Funció que verifica si es pot aplicar UNA alfa-conversió donat una abstracció(var i absTerm) i un terme, 
# retorna l'ABSTRACCIO amb la conversió aplicada si s'escau, sinó retorna l'expressió d'entrada
def alphaconversion(var, absTerm, rightTerm):
    abc = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

    BVabs, usedVarsAbs= boundVariables(Abstraction(var, absTerm))
    if BVabs.count(var) > 1:    
        #En l'abstraccio hi ha solapament de variables lligades
        freeLetters = sorted(abc - usedVarsAbs)
        freshLetter = getNextFreeLetter(var, freeLetters)
        renamedTerm = rename(absTerm, var, freshLetter, False)
        return True, Abstraction(var, renamedTerm)
    else:
        FVright, usedVarsRTerm = freeVariables(rightTerm)

        freeLetters = sorted(abc - (usedVarsAbs | usedVarsRTerm))
        conflictVars = FVright & set(BVabs)

        if conflictVars == set(): 
            #Conjunt buit, no hi ha conflictes, retornem original
            return False, Abstraction(var, absTerm)
        else: 
            #Hi ha conflictes, resolem UN conflicte, canviant la primera variable de l'abstraccio que estigui en el conflicte
            oneConflict = conflictVars.pop()
            freshLetter = getNextFreeLetter(var, freeLetters)
            renamedAbs = rename(Abstraction(var, absTerm), oneConflict, freshLetter, False)
            return True, renamedAbs

#Funció que donada una lletra 'letter' i un conjunt ordenat de lletres,
# retorna la següent lletra de 'letter', en ordre alfàbetic, del conjunt.
# És un procés cíclic, la primera lletra del conjunt "serà" la següent de l'última
def getNextFreeLetter(letter, freeLetters):
    first = True
    firstFree = freeLetters.pop()
    for free in freeLetters:
        if first:
            firstFree = free
            first = False
        if free > letter:
            return free
    return firstFree

#Funcio que retorna dos conjunts ('set' de python) de les variables lliures d'un terme, i les utilitzades en aquest terme(lligades o lliures), respectivament
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

# Funcio que retorna una llista ('list' de python) de les variables lligades d'un terme, i un conjunt de les utilitzades en aquest terme(lligades o lliures)
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

#Funció que donat un Terme/expressió una variable (en conflicte) 'conflict', un nou nom de variable 'newName', i un boolea per com a control de la recursivitat,
# canvia les aparicions PERMESES (per això el boolea per evitar canviar variables lligades més internament que tenen el mateix nom que 'conflict'
#  i que per tant necessitaran una posterior conversió) de la variable 'conflict' per 'newName'
def rename(term, conflict, newName, found):
    match term:
        case Application(left, right):
            newLeft = rename(left, conflict, newName, found)
            newRight = rename(right, conflict, newName, found)
            return Application(newLeft, newRight)
        case Abstraction(var, absTerm):
            if var == conflict and not found:
                #Fiquem found a True ja que hem trobat l'abstracció a la qual farem el re-anomenament"
                newTerm = rename(absTerm, conflict, newName, True)
                return Abstraction(newName, newTerm)
            elif var == conflict and found:
                # Aturem el reanomenament, doncs la variable de l'abstracció actual no es la que estem reanomenant 
                return Abstraction(var, absTerm)
            else:
                newTerm = rename(absTerm, conflict, newName, found)
                return Abstraction(var, newTerm)
        case Letter(letter):
            if found and letter == conflict:
                return Letter(newName)
            else:
                return Letter(letter)
            
######################### BOT TELEGRAM #########################
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Benvingut, estas llest per fer lambda càlculs?!")

async def author(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Pol Mañé Roiger\nQP22/23-LP")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="/start\n/author\n/help\n/macros\nExpressió λ-càlcul")


async def macros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=macrosToStr(macrosDictionary))

async def interact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_stream = InputStream(update.message.text)
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()
    if parser.getNumberOfSyntaxErrors() == 0:
        #Visitor
        visitor = TreeVisitor()
        expression = visitor.visit(tree)
        if expression != 'defMacro':
            textExpr = 'Arbre: \n' + treeToStr(expression)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=textExpr)

            #Evaluator
            maxReductions = 10 #Maximum limit of reductions 

            numReduc = 0
            reducedExpr = expression
            reduced = False
            while numReduc < maxReductions:
                [reduced, reducedExpr, reduction] = evalExpr(reducedExpr)
                if reduced:
                    await context.bot.send_message(chat_id=update.effective_chat.id, text=reduction)
                    numReduc = numReduc + 1
                else:
                    break
            #Result
            if reduced and numReduc >= maxReductions:
                await context.bot.send_message(chat_id=update.effective_chat.id, text='Resultat:\nNothing')
            else:
                textResult = 'Resultat:\n' + treeToStr(reducedExpr)
                await context.bot.send_message(chat_id=update.effective_chat.id, text=textResult)
    else:
        syntaxError = str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=syntaxError)
        # print(tree.toStringTree(recog=parser)) #Descomentar per veure per terminal l'arbre amb la gramatica

if __name__ == '__main__':
    TOKEN = open('token.txt').read().strip()
    application = ApplicationBuilder().token(TOKEN).build()

    #Comandes del bot
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    author_handler = CommandHandler('author', author)
    macros_handler = CommandHandler('macros', macros)
    #Interpreta els missatges de l'usuari que no siguin comandes i respon en conseqüència (és a dir, resol una lambda expressió)
    interact_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), interact)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(author_handler)
    application.add_handler(macros_handler)
    application.add_handler(interact_handler)

    application.run_polling()