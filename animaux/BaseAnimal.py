import random
import sys
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
        print("{] ".format(self.cri))
        self.__pause()


    def se_deplace(self):
        """ l'animal se déplace """
        print("{] ".format(self.deplacement))
        self.__pause()

    def mange(self):
        """ l'animal se déplace """
        """ l'animal se déplace """
        print("{] mange")
        self.__pause()

    def dort(self):
        """ l'animal dort """
        print("{] dort")
        self.__pause()

    def __pause(self):
        attente = 0.2 + random.randint(1, 60) / 100
        time.sleep(attente)

