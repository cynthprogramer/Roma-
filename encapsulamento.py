class roupa:
    def __init__(self, cor, estilo):
        self.__cor=cor
        self.__estilo=estilo
    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.__cor=cor
    @property
    def estilo(self):
        return self.__estilo
    @estilo.setter
    def estilo(self, estilo):
        self.__estilo=estilo

quarta=roupa ('rosa', 'blusa')
print(quarta.cor)
print(quarta.estilo)
quinta=str(input('dgite a cor da blusa:'))
quarta.cor=quinta
print(quarta.cor)


