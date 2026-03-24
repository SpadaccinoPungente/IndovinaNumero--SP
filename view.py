import flet as ft


class View(object):
    """
    Classe che gestisce l'interfaccia grafica dell'applicazione "Indovina il Numero".
    """

    def __init__(self, page: ft.Page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        """
        Inizializza e posiziona tutti i widget (controlli) sulla pagina Flet.
        """
        # Titolo dell'applicazione
        self._titolo = ft.Text("Indovina il numero", color="blue", size=24)

        # Campi di testo in sola lettura per mostrare i parametri di gioco
        self._txtNmax = ft.TextField(
            label="Numero Max",
            value=self._controller.getNmax(),
            disabled=True
        )

        self._txtTmax = ft.TextField(
            label="Num tentativi max",
            value=self._controller.getTmax(),
            disabled=True
        )

        self._txtT = ft.TextField(
            label="Tentativi rimanenti",
            disabled=True
        )

        # Prima riga: mostra le impostazioni e lo stato attuale dei tentativi
        self._row1 = ft.Row(controls=[self._txtNmax, self._txtTmax, self._txtT])

        # Campo di testo dove l'utente inserisce il suo tentativo
        self._txtInTentativo = ft.TextField(label="Valore")

        # Bottoni per controllare il flusso del gioco
        self._btnReset = ft.ElevatedButton(
            text="Nuova Partita",
            on_click=self._controller.reset
        )
        self._btnPlay = ft.ElevatedButton(
            text="Indovina",
            on_click=self._controller.play
        )

        # Seconda riga: input dell'utente e bottoni di azione
        self._row2 = ft.Row(controls=[self._txtInTentativo, self._btnReset, self._btnPlay])

        # Lista visuale (ListView) per mostrare lo storico dei messaggi ("Troppo alto", ecc.)
        self._lvOut = ft.ListView(expand=True)

        # Aggiunge tutti gli elementi creati alla pagina e la aggiorna
        self._page.add(self._titolo, self._row1, self._row2, self._lvOut)
        self._page.update()

    def setController(self, controller):
        """
        Associa il controller alla view, permettendo ai bottoni di richiamare
        i metodi corretti per la logica di gioco.
        """
        self._controller = controller

    def update(self):
        """
        Metodo di utilità per forzare l'aggiornamento dell'interfaccia.
        """
        self._page.update()