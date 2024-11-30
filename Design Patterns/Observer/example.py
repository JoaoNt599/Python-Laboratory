class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)
    
    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)
    

class ObserverA:
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__,':: Got', args, 'From', subject)


class ObserverB:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


if __name__ == "__main__":
    subject = Subject()
    obersvera = ObserverA(subject)
    obersverb = ObserverB(subject)
    subject.notifyAll('notification')