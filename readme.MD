# AChurchBot: Avaluador de λ-càlcul

Aquest Bot de telegram s'encarrega d'avaluar λ-expressions i aplicar-hi les adients transformacions: α-conversions i β-reduccions. Utiilitza com a mitjà un Bot de Telegram, que grafica i escriu les expressions i informa dels passos utilitzats.
A més podem definir Macros per fer els càlculs més portables

## Dependències i instal·lació
Aquest bot ha estat creat amb Python3.10 i antlr4. A continuació mostrem les comandes necessàries per satisfer les dependències en un terminal d' Ubuntu 22.04:

Python3:
```bash
sudo apt install python3
```

Antlr4:
```bash
sudo apt install antlr4
```
I ja dependències del propi codi com llibreries o d'altres programes són els següents:

```bash
pip install antlr4-tools

pip install antlr4-python3-runtime

pip install python-telegram-bot

pip install pydot

sudo apt install graphviz
```

També necessitareu crear un Bot de Telegram, recomano que mireu la documentació Botfather (https://core.telegram.org/bots/tutorial, aquest és un breu tutorial per començar). Realment només necessiteu complir fins que us donin un 'TOKEN' que haureu de guardar en un fitxer en el mateix directori que els altres que es digui 'token.txt'.

## Execució
Un cop comptem amb els fitxers del projecte porcedirem a executar-lo de la següent manera:

Executarem la següent comanda per terminal per tal de generar els fitxers necessaris per interpretar la gramàtica
```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor lc.g4
```
I posteriorment executarem la comanda:
```bash
python3 achurch.py
```

Un cop fet això ja estarem llestos per buscar el nostre Bot a Telegram i començar a interactuar amb ell!
Recordeu que perquè el Bot funcioni, una computadora (o servidor) ha d'estar executant el codi!

## Bot de Telegram
Es tracte d'una interacció ben senzilla (diferents "inputs" acceptats)
* /start: Inicia el Bot
* /author: Cita l'autor del Projecte
* /help: Mostra les possibles opcions a escriure
* /macros: Mostra les macros en el sistema
* λ-expressió


## Contribuir

Apte per contribuir-hi!
https://github.com/polmane/lambda_calcul

## Author

Pol Mañé Roiger, LP - QP22/23
