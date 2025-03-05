from fastapi import FastAPI
from controller import pet_controller

app = FastAPI()

app.include_router(pet_controller.router, prefix="/pets", tags=["Pets"])
