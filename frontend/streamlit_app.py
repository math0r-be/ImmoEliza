import streamlit as st
import requests
import json

st.set_page_config(page_title="ImmoEliza", layout="centered")
st.title("ImmoEliza")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        bedroomCount = st.number_input("Number of bedroom", min_value=0, value=3)
        bathroomCount = st.number_input("Number of bathrooms", min_value=0, value=1)
        habitableSurface = st.number_input("Living surface (m²)", min_value=0, value=100)
        landSurface = st.number_input("Land surface (m²)", min_value=0, value=200)
        facedeCount = st.number_input("Facade count", min_value=0, value=2)

    with col2:
        terraceSurface = st.number_input("Surface area (m²)", min_value=0, value=15)
        hasSwimmingPool = st.checkbox("Swimming pool", value=False)
        hasTerrace = st.checkbox("Terrace", value=True)
        buildingConstructionYear = st.number_input("Construction Year", min_value=1800, max_value=2025, value=2010)
        postCode = st.number_input("Postal code", min_value=1000, max_value=9999, value=1000)

    epc_labels = ["A++", "A+", "A", "B", "C", "D", "E", "F", "G"]
    epc_mapping = {label: idx for idx, label in enumerate(epc_labels)}
    # Vérification finale de l'encodage
    assert len(epc_mapping) == 9, "Encodage EPC incorrect"
    selected_epc = st.selectbox("Score EPC", epc_labels, index=4)
    epcScore_encoded = epc_mapping[selected_epc]

    submitted = st.form_submit_button("🔍 Estimate")

if submitted:
    input_data = {
        "bedroomCount": int(bedroomCount),
        "bathroomCount": int(bathroomCount),
        "habitableSurface": float(habitableSurface),
        "landSurface": float(landSurface),
        "facedeCount": facedeCount,  # changé ici aussi
        "terraceSurface": float(terraceSurface),
        "hasSwimmingPool": hasSwimmingPool,
        "hasTerrace": hasTerrace,
        "buildingConstructionYear": int(buildingConstructionYear),
        "postCode": int(postCode),
        "epcScore_encoded": int(epcScore_encoded)
    }
    
#TEST    
    st.subheader("Données envoyées à l'API")
    st.code(json.dumps(input_data, indent=2))
#FIN TEST

    try:
        response = requests.post("https://immo-api.onrender.com/predict", json=input_data)
        if response.status_code == 200:
            predicted_price = response.json()["predicted_price"]
            st.metric(label="Estimated price", value=f"{predicted_price:,.2f} €")
        else:
            st.error(f"Prediction error. Code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
