from pydantic import BaseModel
from typing import Optional, List, Dict

class Pet(BaseModel):
    id: int
    name: str
    age: int

class Node_abb:
    def __init__(self, data: Pet):
        self.data: Pet = data
        self.left: Optional["Node_abb"] = None
        self.right: Optional["Node_abb"] = None

class Abb:
    def __init__(self):
        self.root: Optional[Node_abb] = None

    def insert(self, pet: Pet):
        """Agrega una mascota al ABB ordenada por edad."""
        if self.root is None:
            self.root = Node_abb(pet)
        else:
            self._insert_recursive(self.root, pet)

    def _insert_recursive(self, node: Node_abb, pet: Pet):
        if pet.age < node.data.age:
            if node.left is None:
                node.left = Node_abb(pet)
            else:
                self._insert_recursive(node.left, pet)
        else:
            if node.right is None:
                node.right = Node_abb(pet)
            else:
                self._insert_recursive(node.right, pet)

    def list_in_order(self) -> List[Dict]:
        """Retorna una lista de mascotas con su posición exacta en el ABB."""
        pets_with_position = []
        self._in_order_traversal(self.root, pets_with_position, "raíz", "")
        return pets_with_position

    def _in_order_traversal(self, node: Optional[Node_abb], pets_with_position: List[Dict], position: str, path: str):
        if node is not None:
            if node == self.root:
                position = "raíz"
                path = "raíz"
            pets_with_position.append({
                "id": node.data.id,
                "name": node.data.name,
                "age": node.data.age,
                "position": position,
                "path": path
            })
            self._in_order_traversal(node.left, pets_with_position, f"izquierda de {node.data.id}", f"{path} → izquierda de {node.data.id}")
            self._in_order_traversal(node.right, pets_with_position, f"derecha de {node.data.id}", f"{path} → derecha de {node.data.id}")
