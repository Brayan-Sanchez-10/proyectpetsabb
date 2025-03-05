from fastapi import APIRouter, HTTPException
from model.pet import Pet, Abb

router = APIRouter()

# Lista en memoria para almacenar las mascotas (método original)
pets = []

# Instancia del Árbol Binario de Búsqueda (ABB)
abb = Abb()

@router.post("/")
def create_pet(pet: Pet):
    """Agrega una mascota tanto a la lista como al ABB."""
    # Verificar si el ID ya existe en la lista
    for existing_pet in pets:
        if existing_pet["id"] == pet.id:
            raise HTTPException(status_code=400, detail="Pet ID already exists")

    # Agregar a la lista
    new_pet = {"id": pet.id, "name": pet.name, "age": pet.age}
    pets.append(new_pet)

    # Agregar al ABB
    abb.insert(pet)

    return new_pet

@router.get("/")
def list_pets():
    """Lista todas las mascotas de la lista original."""
    return pets

@router.get("/sorted/")
def list_pets_sorted():
    """Lista todas las mascotas ordenadas por edad e indica su posición en el ABB."""
    return abb.list_in_order()

@router.get("/{pet_id}")
def get_pet(pet_id: int):
    """Busca una mascota en la lista por su ID."""
    for pet in pets:
        if pet["id"] == pet_id:
            return pet
    raise HTTPException(status_code=404, detail="Pet not found")

@router.put("/{pet_id}")
def update_pet(pet_id: int, pet: Pet):
    """Actualiza los datos de una mascota en la lista."""
    for existing_pet in pets:
        if existing_pet["id"] == pet_id:
            existing_pet["name"] = pet.name
            existing_pet["age"] = pet.age
            return existing_pet
    raise HTTPException(status_code=404, detail="Pet not found")

@router.delete("/{pet_id}")
def delete_pet(pet_id: int):
    """Elimina una mascota de la lista por ID."""
    global pets
    pets = [pet for pet in pets if pet["id"] != pet_id]
    return {"message": "Pet deleted successfully"}

@router.delete("/by_age/{age}")
def delete_pet_by_age(age: int):
    """Elimina una mascota del ABB por edad."""
    abb.delete(age)
    return {"message": f"Pet with age {age} deleted successfully"}

@router.get("/average_age/")
def get_average_age():
    """Calcula el promedio de edad de las mascotas en la lista."""
    if not pets:
        return {"average_age": 0}
    total_age = sum(pet["age"] for pet in pets)
    return {"average_age": total_age / len(pets)}