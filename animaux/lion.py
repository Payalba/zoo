from animaux.baseanimal import BaseAnimal

class Lion(BaseAnimal):

    def __init__(self):
        BaseAnimal.__init__(self, "Leo le lion", "rugit", "court")
