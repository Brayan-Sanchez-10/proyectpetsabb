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

    def update(self, pet:Pet, id: int):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            self.root.update(pet, id)

    def inorder(self):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            return self.root.get_inorder()

    def delate(self, id, pet: Pet):
        if self.root == None:
            return "El arbol esta vacio"
        else:
            return self.root.delate(id)

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



    #Actualizar mascota por id
    def update(self, pet: Pet, id: int):
        if self.pet.id == id:
            self.pet.name = pet.name
            self.pet.age = pet.age
            self.pet.race = pet.race
        elif id < self.pet.id:
            if self.left:
                self.left.update(pet, id)
            else:
                raise Exception("No se encontró la mascota con el ID dado.")
        elif id > self.pet.id:
            if self.right:
                self.right.update(pet, id)
            else:
                raise Exception("No se encontró la mascota con el ID dado.")

    #Borrar mascota:
    def delete(self, id):
        if id < self.pet.id:
            if self.left:
                self.left = self.left.delete(id)
            else:
                raise Exception(f"No se encontró la mascota con ID {id}")
            return self

        elif id > self.pet.id:
            if self.right:
                self.right = self.right.delete(id)
            else:
                raise Exception(f"No se encontró la mascota con ID {id}")
            return self

        else:
            mascotas_a_reinsertar = []
            if self.left:
                mascotas_a_reinsertar += self.left.get_preorder()
            if self.right:
                mascotas_a_reinsertar += self.right.get_preorder()

            print(f"Mascota con ID {id} eliminada")

            nuevo_root = None
            for pet in mascotas_a_reinsertar:
                if nuevo_root is None:
                    nuevo_root = NodeABB(pet)
                else:
                    nuevo_root.add(pet)

            return nuevo_root

    def get_inorder(self):
        listPets = []
        if self.left is not None:
            listPets += self.left.get_inorder()
        listPets.append(self.pet)
        if self.right is not None:
            listPets += self.right.get_inorder()
        return listPets

    def get_preorder(self):
        listPets = [self.pet]
        if self.left != None:
            listPets += self.left.get_preorder()
        if self.right != None:
            listPets += self.right.get_preorder()
        return listPets

    def get_postorden(self):
        listPets = []
        if self.left != None:
            listPets += self.left.get_postorden()
        if self.right != None:
            listPets += self.right.get_postorden()
        listPets.append(self.pet)
        return listPets



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