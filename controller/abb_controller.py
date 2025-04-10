from model.pet import Pet
from service import abb_service
from fastapi import APIRouter,  Response, status

abb_service = abb_service.ABBService()

abb_route = APIRouter(prefix="/abb")

@abb_route.get("/")
async def get_pets():
    return abb_service.abb.root

@abb_route.get("/inorder")
async def get_pets_inorder():
    try:
        return abb_service.abb.inorder()
    except Exception as e:
        return {"message":e.args[0]}

@abb_route.get("/preorder")
async def get_pets_preorder():
    try:
        return abb_service.abb.root.get_preorder()
    except Exception as e:
        return {"message": e.args[0]}

@abb_route.get("/postorder")
async def get_pets_postorder():
    try:
        return abb_service.abb.root.get_postorden()
    except Exception as e:
        return {"message": e.args[0]}
@abb_route.post("/", status_code=200)
async def create_pet(pet:Pet, response: Response):
    try:
        abb_service.abb.add(pet)
        return {"message":"Adicionado exitosamente"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message":e.args[0]}

@abb_route.put("/{id}")
async def update_pet(id: int, pet: Pet, response: Response):
    try:
        abb_service.abb.update(pet,id)
        return {"message": "Actualizado exitosamente"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.args[0]}

#Eliminar mascota por id
@abb_route.delete("/{id}")
async def delete_pet(id: int):
    if abb_service.abb.root is None:
        raise HTTPException(status_code=404, detail="El árbol está vacío")

    abb_service.abb.root = abb_service.abb.root.delete(id)
    return {"message": "Mascota eliminada correctamente"}

#Actualizar mascota por id


#listar por razas
@abb_route.get("/races")
async def get_race_count():
    if not abb_service.abb.root:
        raise HTTPException(status_code=404, detail="El árbol está vacío")

    race_counts = abb_service.abb.root.list_race()
    return {"races": race_counts}