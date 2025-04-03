from model.pet import Pet
from fastapi import HTTPException
from service import abb_service
from fastapi import APIRouter

abb_service = abb_service.ABBService()

abb_route = APIRouter(prefix="/abb")

@abb_route.get("/")
async def get_pets():
    return abb_service.abb.root

@abb_route.post("/")
async def create_pet(pet: Pet):
    result = abb_service.abb.add(pet)
    if result == "id erroneo":
        raise HTTPException(status_code=400, detail="El ID de la mascota ya existe")
    return {"message": "Mascota adicionada correctamente"}


#obtener una mascota por id
@abb_route.get("/{id}")
async def get_pet(id: int):
    node = abb_service.abb.root
    while node:
        if id < node.pet.id:
            node = node.left
        elif id > node.pet.id:
            node = node.right
        else:
            return node.pet  # Se encontró la mascota
    raise HTTPException(status_code=404, detail="Mascota no encontrada")

#Eliminar mascota por id
@abb_route.delete("/{id}")
async def delete_pet(id: int):
    if abb_service.abb.root is None:
        raise HTTPException(status_code=404, detail="El árbol está vacío")

    abb_service.abb.root = abb_service.abb.root.delete(id)
    return {"message": "Mascota eliminada correctamente"}

#Actualizar mascota por id
@abb_route.put("/{id}")
async def update_pet(id: int, pet: Pet):
    if abb_service.abb.root is None:
        raise HTTPException(status_code=404, detail="El árbol está vacío")

    abb_service.abb.root.update(id, pet)
    return {"message": "Mascota actualizada correctamente"}

#listar por razas
@abb_route.get("/races")
async def get_race_count():
    if not abb_service.abb.root:
        raise HTTPException(status_code=404, detail="El árbol está vacío")

    race_counts = abb_service.abb.root.list_race()
    return {"races": race_counts}