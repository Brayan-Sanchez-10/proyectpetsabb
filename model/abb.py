from model.pet import Pet

class ABB():
    def __init__(self):
        self.root = None

    def add(self, pet: Pet):
        if self.root == None:
            self.root = NodeABB(pet)
            return "Adicionado"
        else:
            return self.root.add(pet)

class NodeABB:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1
    #Agregar mascota y validacion de id
    def add(self, pet: Pet):
        if pet.id < self.pet.id:
            if self.left != None:
                result = self.left.add(pet)
                if result == "Adicionado":
                    self.size += 1
                return result
            else:
                self.left = NodeABB(pet)
                self.size += 1
                return "Adicionado"

        elif pet.id > self.pet.id:
            if self.right != None:
                result = self.right.add(pet)
                if result == "Adicionado":
                    self.size += 1
                return result
            else:
                self.right = NodeABB(pet)
                self.size += 1
                return "Adicionado"
        # id incorrecto
        else:
            return "id erroneo"

    #borrar mascota
    def delete(self, id):
        if id < self.pet.id:  #Buscar en la izquierda
            if self.left:
                self.left = self.left.delete(id)
            return self

        elif id > self.pet.id:  #Buscar en la derecha
            if self.right:
                self.right = self.right.delete(id)
            return self

        else:  #Encontramos el nodo a eliminar
            if self.left == None:  #Solo tiene hijo derecho o esta solo
                return self.right
            if self.right == None:  #Solo tiene hijo izquierdo
                return self.left

            #Si tiene dos hijos, se reemplaza con el menor de la derecha
            min_node = self.right.get_min()
            self.pet = min_node.pet
            self.right = self.right.delete(min_node.pet.id)
            return self

    # Encuentra el menor en el subarbol derecho para que se remplace por el eliminado
    def get_min(self):
        if self.left == None:
            return self
        return self.left.get_min()

    #Actualizar mascota por id
    def update(self, id, pet: Pet):
        if id < self.pet.id:  # Buscar en la izquierda
            if self.left:
                self.left.update(id, pet)
            else:
                print(f"No se encontró una mascota con ID {id}")
        elif id > self.pet.id:  # Buscar en la derecha
            if self.right:
                self.right.update(id, pet)
            else:
                print(f"No se encontró una mascota con ID {id}")
        else:  # Si encontramos el nodo con el ID correspondiente
            self.pet = pet  # Se actualiza la mascota sin modificar la estructura

        return self

    #Listar mascotas por raza
    def list_race(self, races=None):
        if races is None:
            races = {}
        if self.pet.race in races:
            races[self.pet.race] += 1
        else:
            races[self.pet.race] = 1
        if self.left:
            self.left.list_race(races)
        if self.right:
            self.right.list_race(races)

        return races

class NodeAVL(NodeABB):
    def __init__(self, pet:Pet):
        super().__init__(pet)
        self.height = 1
        self.balance = 1