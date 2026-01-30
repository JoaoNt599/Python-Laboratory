class Subject:
    def __init__(self):
        self._observers = []

    def adicionar_observador(self, observer):
        self._observers.append(observer)

    def remover_observador(self, observer):
        self._observers.remove(observer)

    def notificar_observadores(self):
        for observer in self._observers:
            observer.atualizar(self)


class NewsAgency(Subject):
    def __init__(self):
        super().__init__()
        self._headline = ""

    @property
    def headline(self):
        return self._headline

    @headline.setter
    def headline(self, value):
        self._headline = value
        self.notificar_observadores()


class Screen:
    def atualizar(self, subject):
        print(f"Tela atualizada com a manchete: {subject.headline}")


if __name__ == "__main__":
    agency = NewsAgency()
    screen1 = Screen()
    screen2 = Screen()

    agency.adicionar_observador(screen1)
    agency.adicionar_observador(screen2)

    agency.headline = "Nova manchete"
