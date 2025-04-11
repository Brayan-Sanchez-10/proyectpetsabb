from model.pet import Pet
from service import abb_service
from fastapi import APIRouter,  Response, status

abb_service = abb_service.ABBService()

abb_route = APIRouter(prefix="/abb")

#listar abb:
@abb_route.get("/")
async def get_pets():
    return abb_service.abb.root

#Listar inorder:
@abb_route.get("/inorder")
async def get_pets_inorder():
    try:
        return abb_service.abb.inorder()
    except Exception as e:
        return {"message":e.args[0]}

#Listar preorder:
@abb_route.get("/preorder")
async def get_pets_preorder():
    try:
        return abb_service.abb.preorder()
    except Exception as e:
        return {"message": e.args[0]}

#Listar postorder:
@abb_route.get("/postorder")
async def get_pets_postorder():
    try:
        return abb_service.abb.postorder()
    except Exception as e:
        return {"message": e.args[0]}

#Crear mascota:
@abb_route.post("/", status_code=200)
async def create_pet(pet: Pet, response: Response):
    result = abb_service.abb.add(pet)

    if result == "Adicionado":
        return {"message": "Adicionado exitosamente"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": result}

#Editar mascota:
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

#Eliminar por nivel:
@abb_route.delete("/delete_by_level/{level}")
async def delete_nodes_by_level(level: int):
    try:
        message = abb_service.abb.delete_by_level(level)
        return {"message": message}
    except Exception as e:
        return {"message": e.args[0]}

#listar por razas
@abb_route.get("/races")
async def get_race_count():
    race_counts = abb_service.abb.list_race()
    if not race_counts:
        return {"message": "El árbol está vacío", "races": {}}
    return {"races": race_counts}

#Reporte de mascotas por ciudad:
@abb_route.get("/report_by_location_gender")
async def report_by_location_gender():
    return abb_service.abb.report_by_location_gender()

