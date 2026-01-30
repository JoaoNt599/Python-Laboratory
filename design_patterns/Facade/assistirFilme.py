

class DVDPlayer(object):
    def __init__(self):
        print("Verificando DVD Player...\n")
    
    def ligar(self): 
        print("DVD Player ligado.")
    
    def reproduzir(self): 
        print("Reproduzindo DVD.\n\n")


class TV(object):
    def __init__(self):
        print("Verificando TV... \n")

    def ligar(self): 
        print("TV ligada.")
    
    def ajustar_resolucao(self): 
        print("Resolução ajustada.\n\n")


class AltoFalantes(object):
    def __init__(self):
        print("Verificando Altos-falantes...\n")

    def ligar(self): 
        print("Alto-falantes ligados.")
    
    def ajustar_volume(self): 
        print("Volume ajustado.\n\n")


class HomeTheaterFacade(object):
    def __init__(self):
        self.dvd = DVDPlayer()
        self.tv = TV()
        self.som = AltoFalantes()

    def assistir_filme(self):
        print("Configurando sistema para assistir filme \n\n")
        self.dvd.ligar()
        self.dvd.reproduzir()
        self.tv.ligar()
        self.tv.ajustar_resolucao()
        self.som.ligar()
        self.som.ajustar_volume()
        print("Pronto! Hora do filme!\n\n")


if __name__ == "__main__":
    home_theater = HomeTheaterFacade()
    home_theater.assistir_filme()
