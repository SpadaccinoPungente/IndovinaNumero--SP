import random


class Model(object):
    """
    Gestisce la logica di business e lo stato del gioco "Indovina il Numero".
    """

    def __init__(self):
        self._Nmax = 100
        self._Tmax = 6
        self._T = self._Tmax  # Tentativi correnti
        self._segreto = None

    def reset(self):
        """
        Resetta lo stato del gioco. Imposta il segreto a un valore randomico
        tra 1 e NMax (incluso) e ripristina il numero di tentativi rimanenti.
        """
        # Modificato da (0, Nmax) a (1, Nmax) per rispettare le specifiche
        self._segreto = random.randint(1, self._Nmax)
        self._T = self._Tmax

        # Stampa il segreto nel terminale (utile per fare test in fase di sviluppo)
        print(f"[DEBUG] Il numero segreto generato è: {self._segreto}")

    def play(self, tentativo):
        """
        Riceve il tentativo del giocatore e lo confronta con il numero segreto.

        Ritorna:
         0 : se il tentativo è uguale al segreto (Vittoria)
         2 : se non ci sono più tentativi disponibili (Sconfitta)
        -1 : se il segreto è più piccolo del tentativo
         1 : se il segreto è più grande del tentativo
        """
        # Se i tentativi sono già a zero prima di giocare, non permette di continuare
        if self._T == 0:
            return 2

        # Decrementa il numero di tentativi disponibili
        self._T -= 1

        if tentativo == self._segreto:
            # L'utente ha indovinato
            return 0

        if self._T == 0:
            # L'utente ha sbagliato l'ultimo tentativo disponibile
            return 2

        if tentativo > self._segreto:
            # Il tentativo è troppo alto
            return -1
        else:
            # Il tentativo è troppo basso
            return 1

    # Utilizzo dei decoratori @property per accedere in modo sicuro alle variabili di stato
    @property
    def Nmax(self):
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto


# Blocco eseguito solo se il file viene lanciato direttamente (utile per testare il Model)
if __name__ == "__main__":
    m = Model()
    m.reset()
    # Esegue una serie di test fittizi per verificare le risposte del metodo play
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(70))
    print(m.play(80))
    print(m.play(60))
    print(m.play(50))

