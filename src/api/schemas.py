# Définit les schémas de validation des entrées/sorties avec Pydantic
from pydantic import BaseModel

class PropertyFeatures(BaseModel):
    bedroomCount: int
    bathroomCount: int
    habitableSurface: float
    landSurface: float
    facedeCount: int
    terraceSurface: float
    hasSwimmingPool: bool
    hasTerrace: bool
    buildingConstructionYear: int
    postCode: int
    epcScore_encoded: float

    # Tu peux ajouter les colonnes one-hot encodées ici plus tard si besoin
