import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import pickle
import os

# Chemin vers le fichier CSV
DATA_PATH = os.path.join(os.path.dirname(__file__), "../../data/Kangaroo_cleaned.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = [
        'bedroomCount', 'bathroomCount', 'habitableSurface', 'landSurface',
        'facedeCount', 'terraceSurface', 'hasSwimmingPool', 'hasTerrace',
        'buildingConstructionYear', 'price', 'postCode'
    ]
    categorical_cols = ['buildingCondition', 'heatingType', 'kitchenType', 'province']
    epc_col = 'epcScore'

    # Sélection des colonnes utiles
    cols = [c for c in numeric_cols if c in df.columns]
    if epc_col in df.columns:
        cols.append(epc_col)
    cols += [c for c in categorical_cols if c in df.columns]
    df = df[cols].dropna().copy()

    # Encodage ordinal pour epcScore
    if epc_col in df.columns:
        epc_order = ['A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        enc = OrdinalEncoder(categories=[epc_order], handle_unknown='use_encoded_value', unknown_value=-1)
        df['epcScore_encoded'] = enc.fit_transform(df[[epc_col]])
        df.drop(columns=[epc_col], inplace=True)

    # One-hot encoding
    df = pd.get_dummies(df, columns=[c for c in categorical_cols if c in df.columns], drop_first=True)
    return df

def train_and_save_model():
    df = pd.read_csv(DATA_PATH)
    df = preprocess_data(df)
    X = df.drop(columns=["price"])
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=50, max_depth=15, random_state=42)
    model.fit(X_train, y_train)

    # Sauvegarde du modèle
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print("✅ Modèle entraîné et sauvegardé dans :", MODEL_PATH)

    # Sauvegarde des noms de colonnes
    feature_path = os.path.join(os.path.dirname(__file__), "model_features.csv")
    X_train.to_csv(feature_path, index=False)
    print("✅ Features sauvegardées dans :", feature_path)

if __name__ == "__main__":
    train_and_save_model()
