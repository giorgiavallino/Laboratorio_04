# Importare i moduli necessari per lo svolgimento del programma
import time
import flet as ft
import model as md
from view import View

# Definire una classe Controller che prende il nome di SpellChecker
class SpellChecker:

    # Definire un metodo __init__ contenente il modello e la view, che permetta a questi due elementi di comunicare
    # tramite il controller
    def __init__(self, view: View):
        self._multiDic = md.MultiDictionary()
        self._view = view

    # Definire un metodo handleSentence
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

    # Definire un modello printMenu
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

    # Definire un metodo handleLangSelection che gestisca il corretto inserimento della lingua scelta
    def handleLangSelection(self):
        self._view._lvOut.controls.append(ft.Text("Language selected: " + self._view._dropdown_lingua.value)) # stampa
        # la lingua scelta nell'interfaccia grafica per far capire all'utente che il selezionamento è stato fatto
        # correttamente
        self._view.update()

    # Definire un metodo handleResearchMethodSelection che gestisca il corretto inserimento della modalità di ricerca
    # scelta
    def handleResearchMethodSelection(self):
        self._view._lvOut.controls.append(ft.Text("Research method selected: " + self._view._dropdown_lingua.value))
        # stampa il metodo di ricerca scelto nell'interfaccia grafica per far capire all'utente che il selezionamento è
        # stato fatto correttamente
        self._view.update()

    # Definire un metodo handleSpellChecker che gestisca ciò che succede quando viene cliccato il button per la
    # correzione --> gestione degli input, indicazione delle parole sbagliate e calcolo del tempo impiegato per ottenere
    # le parole errate nella frase
    def handleSpellChecker(self):

        # Gestione dell'input dropdown_lingua: controllare che l'input sia presente
        language = self._view._dropdown_lingua.value
        if language == "":
            self._view._lvOut.controls.clear()
            self._view._lvOut.controls.append(ft.Text("Please select a language!", color = "red"))
            self._view.update()
            return
        self._view._dropdown_lingua.controls.clear()

        # Gestione dell'input dropdown_ricerca: controllare che l'input sia presente
        method = self._view._dropdown_ricerca.value
        if method == "":
            self._view._lvOut.controls.clear()
            self._view._lvOut.controls.append(ft.Text("Please select a research method!", color = "red"))
            self._view.update()
            return
        self._view._dropdown_ricerca.controls.clear()

        # Gestione dell'input testo_iniziale: controllare che l'input sia presente e cancellare l'input inserito per
        # avere di nuovo una text.field bianca, senza testo
        testo_da_correggere = self._view._testo_iniziale.value
        if testo_da_correggere == "":
            self._view._lvOut.controls.clear()
            self._view._lvOut.controls.append(ft.Text("Please enter a sentence to correct!", color = "red"))
            self._view.update()
            return
        self._view._testo_iniziale.controls.clear()
        self._view.update()

        # Determinare le parole sbagliate e il tempo impiegato per trovarle con la funzione handleSentence
        parole_sbagliate, tempo = self.handleSentence(testo_da_correggere, language, method)

        # Ripulire la ListView e aggiornarla con i dati richiesti dall'esercizio: la frase iniziale, le parole
        # sbagliate e il tempo impiegato per trovarle
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Initial sentence: " + testo_da_correggere))
        self._view._lvOut.controls.append(ft.Text("Wrong words: " + parole_sbagliate))
        self._view._lvOut.controls.append(ft.Text("Time needed: " + tempo))

        self._view.update()

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text