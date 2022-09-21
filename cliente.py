class Cliente:

    def __init__(self, nome):
        print("construindo objeto ... {}".format(self))
        self.__nome = nome

    @property  # getter #
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando @setter nome()")
        self.__nome = nome
