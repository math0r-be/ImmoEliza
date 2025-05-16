from pydantic import BaseModel

class PropertyFeatures(BaseModel):
    bedroomCount: int
    bathroomCount: int
    habitableSurface: float
    landSurface: float
    facedeCount: int  # renommé
    terraceSurface: float
    hasSwimmingPool: bool
    hasTerrace: bool
    buildingConstructionYear: int
    postCode: int
    epcScore_encoded: float
