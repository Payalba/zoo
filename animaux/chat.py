from animaux.baseanimal import BaseAnimal

class Chat(BaseAnimal):

    def __init__(self):
        BaseAnimal.__init__(self,"Pussy le chat","miaule","marche")
