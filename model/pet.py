from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    name: str
    age: int
    race: str
    location: str
    gender: str

    def __init__(self, **data):
        super().__init__(**data)

        if not self.name.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede tener letras y espacios")

        if not self.race.replace(" ", "").isalpha():
            raise ValueError("La raza solo puede tener letras y espacios")

        if not self.location.replace(" ", "").isalpha():
            raise ValueError("La ciudad solo puede tener letras y espacios")

        if self.gender.lower() not in ["macho", "hembra"]:
            raise ValueError("El género debe ser 'macho' o 'hembra'")
