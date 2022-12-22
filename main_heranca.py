class Animal:
    def __init__(self,patas,peso):
        self.patas=patas
        self.peso=peso
    
    def andar(self):
        print("andando...")

class Cachorro(Animal):
    def __init__(self, patas, peso):
        super().__init__(patas, peso)

    def latir(self):
        print("latindo...")

class Gato(Animal):
    def miar(self):
        print("miando")



cachorro1 = Cachorro(4,10)
cachorro1.latir()

gato1 = Gato(4,3)
gato1.miar()






    

