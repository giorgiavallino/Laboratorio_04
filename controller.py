# Importare i moduli necessari per lo svolgimento del programma
import time
import flet as ft
import model as md
from view import View

class SpellChecker:

    def __init__(self, view: View):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleLangSelection(self):
        self._view._lvOut.controls.append(ft.Text("Language selected: " + self._view._dropdown_lingua.value))
        self._view.update()

    def handleResearchMethodSelection(self):
        self._view._lvOut.controls.append(ft.Text("Research method selected: " + self._view._dropdown_lingua.value))
        self._view.update()

    def handleSpellChecker(self):

        language = self._view._dropdown_lingua.value
        if language == "":
            self._view._lvOut.controls.append(ft.Text("Please select a language!", color = "red"))
            self._view.update()

        method = self._view._dropdown_ricerca.value
        if method == "":
            self._view._lvOut.controls.append(ft.Text("Please select a research method!", color = "red"))

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text