from model.abb import ABB
from model.pet import Pet


class ABBService():
    def __init__(self):
        self.abb = ABB()
        # llenar ABB

        self.abb.add(Pet(id=7,name="Lulu",age=13, race= "pastor"))
        rocky = Pet(id=2,name="Rocky",age=5, race= "labrador")
        self.abb.add(rocky)