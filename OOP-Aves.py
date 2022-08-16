
class Animal:
    def __init__(self):
        self.__n_de_patas = -1
        self.__tem_asas = False

    @property
    def numeros_patas(self):
        return self.__n_de_patas
    @property
    def tem_asas(self):
        return self.__tem_asas
    
    def emiteSom(self):
        print("-----")

class Cachorro(Animal):
    def __init__(self):
        self.__n_de_patas = 4
        self.__tem_asas = False
    
    @property
    def numeros_patas(self):
        return self.__n_de_patas
    @property
    def tem_asas(self):
        return self.__tem_asas

    def fazer_truques(self):
        print("senta deita")

class Gato(Animal):
    def __init__(self):
        self.__n_de_patas = 4
        self.__tem_asas = False
    
    @property
    def numeros_patas(self):
        return self.__n_de_patas           
    
    @property
    def tem_asas(self):
        return self.__tem_asas

    def emiteSom(self):
        print("miau")

class Calopsita(Animal):
    def __init__(self):
        self.__n_de_patas = 2
        self.__tem_asas = True

    @property
    def tem_asas(self):
        return self.__tem_asas

    @property
    def numeros_patas(self):
        return self.__n_de_patas
    def emiteSom(self):
        print("piii")

    def voar(self):
        print('voando')    
    
def processar_animal(animal: Animal):
    print(f"Este animal tem {animal.numeros_patas} patas")
    print(f"este animal tem {animal.tem_asas} asas")
    animal.emiteSom()
    if isinstance(animal, Calopsita):
        animal.voar()
    if isinstance(animal, Cachorro):
        animal.fazer_truques()
cachorro=Cachorro()
gato=Gato()
calopsita=Calopsita()
processar_animal(cachorro)
processar_animal(gato)
processar_animal(calopsita)