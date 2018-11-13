import random
from threading import Thread
import time

class BaseAnimal(Thread):
    """ CLass abstraite mère de tous les animaux du zoo"""

    def __init__(self,nom,cri,deplacement):
        Thread.__init__(self)
        self.cri = cri
        self.deplacement = deplacement
        self.nom = nom

    def crie(self):
        """ l'animal criie """
        print("{} {}".format(self.nom,self.cri))
        self.__pause()


    def se_deplace(self):
        """ l'animal se déplace """
        print("{} {}".format(self.nom,self.deplacement))
        self.__pause()

    def mange(self):
        """ l'animal se déplace """
        print("{} mange".format(self.nom))
        self.__pause()

    def dort(self):
        """ l'animal dort """
        print("{} dort".format(self.nom))
        self.__pause()

    def __pause(self):
        attente = 0.2 + random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):
        """ vie de l'animal"""
        i = 0
        while i < 20:
            self.crie()
            self.mange()
            self.se_deplace()
            self.dort()
            i+=1