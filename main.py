from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

modelo = joblib.load("arbol-vinoTinto.pkl")

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada
class Vino(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(vino: Vino):
    data = np.array([[ 
        vino.fixed_acidity,
        vino.volatile_acidity,
        vino.citric_acid,
        vino.residual_sugar,
        vino.chlorides,
        vino.free_sulfur_dioxide,
        vino.total_sulfur_dioxide,
        vino.density,
        vino.pH,
        vino.sulphates,
        vino.alcohol
    ]])
    
    prediction = modelo.predict(data)[0]
    calidad = "Buena calidad" if prediction == 1 else "Mala calidad"
    
    return {
        "predicción": int(prediction),
        "mensaje": calidad
    }
