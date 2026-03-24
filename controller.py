import flet as ft
from view import View
from model import Model


class Controller(object):
    """
    Gestisce le interazioni tra l'interfaccia grafica (View) e la logica di business (Model).
    """

    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def reset(self, e):
        """
        Gestisce l'evento di inizio di una nuova partita.
        """
        # Resetta lo stato del gioco lato modello
        self._model.reset()

        # Aggiorna la vista con il numero di tentativi iniziali
        self._view._txtT.value = self._model.T

        # Pulisce lo storico dei messaggi e inserisce quello iniziale
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(
            ft.Text("Inizia il gioco! Indovina a quale numero sto pensando.")
        )

        # Pulisce il campo di input per comodità dell'utente
        self._view._txtInTentativo.value = ""
        self._view.update()

    def play(self, e):
        """
        Gestisce l'evento del tentativo di indovinare il numero.
        """
        tentativoStr = self._view._txtInTentativo.value

        # Validazione dell'input: si assicura che l'utente abbia inserito un numero intero
        try:
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Errore, devi inserire un valore numerico valid!", color="red")
            )
            self._view.update()
            return

        # Passa il tentativo al modello e ottiene il risultato della giocata
        res = self._model.play(tentativo)

        # Aggiorna il numero di tentativi rimanenti visualizzati nell'interfaccia
        self._view._txtT.value = self._model.T

        # Analizza il risultato restituito dal modello e aggiorna l'interfaccia
        if res == 0:
            # L'utente ha indovinato il numero
            self._view._lvOut.controls.append(
                ft.Text(f"Hai vinto! Il valore corretto era proprio {tentativo}.", color="green")
            )
        elif res == 2:
            # L'utente ha esaurito i tentativi disponibili
            self._view._lvOut.controls.append(
                ft.Text(f"Hai perso! Il valore corretto era {self._model.segreto}.", color="red")
            )
        elif res == -1:
            # Il numero segreto è minore del tentativo inserito
            self._view._lvOut.controls.append(
                ft.Text(f"Nope! Il numero segreto è più piccolo di {tentativo}.")
            )
        else:
            # Il numero segreto è maggiore del tentativo inserito (res == 1)
            self._view._lvOut.controls.append(
                ft.Text(f"Nope! Il numero segreto è più grande di {tentativo}.")
            )

        # Pulisce l'input per il prossimo tentativo e aggiorna la pagina
        self._view._txtInTentativo.value = ""
        self._view.update()

    def getNmax(self):
        """Restituisce il valore massimo possibile per il numero segreto."""
        return self._model.Nmax

    def getTmax(self):
        """Restituisce il numero massimo di tentativi permessi."""
        return self._model.Tmax