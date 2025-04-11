from model.abb import ABB
from model.pet import Pet


class ABBService():
    def __init__(self):
        self.abb = ABB()
        # llenar ABB

        self.abb.add(Pet(id=7,name="Lulu",age=13, race= "pastor", location= "manizales", gender= "hembra"))
        rocky = Pet(id=3,name="Rocky",age=5, race= "labrador", location= "Chinchina", gender= "macho")
        self.abb.add(rocky)

