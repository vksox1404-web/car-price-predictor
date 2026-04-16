import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Qatar Car Price AI",
    page_icon="🚗",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.stApp { background: #0a0a0f; color: #e8e6e0; }

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 600px;
}

.app-header {
    text-align: center;
    margin-bottom: 2.5rem;
    padding: 2rem 0 1.5rem;
    border-bottom: 1px solid #1e1e2a;
}

.app-header h1 {
    font-size: 2rem;
    font-weight: 600;
    color: #f0ede8;
    margin: 0 0 0.5rem;
    letter-spacing: -0.02em;
    line-height: 1.2;
}

.app-header p {
    font-size: 14px;
    color: #6b6b7a;
    margin: 0;
}

.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    color: #4a4a5a;
    text-transform: uppercase;
    margin: 1.5rem 0 0.75rem;
}

.result-card {
    background: linear-gradient(135deg, #0f1923 0%, #0a1520 100%);
    border: 1px solid rgba(74,158,255,0.25);
    border-radius: 16px;
    padding: 1.75rem;
    margin-top: 1.5rem;
    text-align: center;
}

.result-card .label {
    font-size: 12px;
    color: #4a9eff;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.1em;
    margin-bottom: 0.5rem;
}

.result-card .price {
    font-size: 2.75rem;
    font-weight: 600;
    color: #f0ede8;
    letter-spacing: -0.03em;
    line-height: 1;
    margin-bottom: 0.5rem;
}

.result-card .sub { font-size: 13px; color: #4a4a5a; }

.result-card .accuracy {
    display: inline-block;
    margin-top: 1rem;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #2dd4a0;
    background: rgba(45,212,160,0.08);
    border: 1px solid rgba(45,212,160,0.2);
    padding: 4px 12px;
    border-radius: 20px;
}

div[data-testid="stButton"] > button {
    background: #4a9eff !important;
    color: #000 !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    padding: 0.65rem 2rem !important;
    width: 100% !important;
}
</style>

<div class="app-header">
    <h1>Qatar Car<br>Price Predictor</h1>
    <p>Instant price estimates powered by machine learning</p>
</div>
""", unsafe_allow_html=True)

model   = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Brand → Models mapping from the dataset
brand_models = {
    "Audi":       ["A3","A4","A5","A6","A7","A8","Q5","Q7","S5","S8"],
    "BMW":        ["The 1","The 3","The 4","The 5","The 7","The M","X","Z"],
    "Cadillac":   ["ATS","CT5","CT6","Escalade","SRX","XT5"],
    "Chevrolet":  ["Avalanche","Aveo","Blazer","Camaro","Caprice","Colorado","Cruze","Impala","Malibu","Silverado","Suburban","Tahoe","Trailblazer"],
    "Chrysler":   ["300","C300","Grand Voyager","SRT"],
    "Dodge":      ["Challenger","Charger","Durango","Ram"],
    "Ford":       ["Bronco","Edge","Expedition","Explorer","F150","Focus","Fusion","Mustang","Ranger"],
    "GMC":        ["Acadia","Envoy","Sierra","Suburban","Terrain","Yukon"],
    "Honda":      ["Accord","CRV","City","Civic","HRV","Odyssey","Pilot"],
    "Hyundai":    ["Accent","Azera","Creta","Elantra","H1","Kona","Palisade","Santa Fe","Sonata","Tucson","Veloster"],
    "Jeep":       ["Cherokee","Commander","Compass","Grand Cherokee","Wrangler"],
    "Kia":        ["Cadenza","Carnival","Cerato","K5","Mohave","Optima","Picanto","Rio","Sorento","Sportage","Telluride"],
    "Land Rover": ["Defender","Discovery","Range Rover"],
    "Lexus":      ["ES","GS","GX","IS","LS","LX","NX","RC","RX","UX"],
    "Mazda":      ["2","3","6","CX3","CX5","CX7","CX9"],
    "Mercedes":   ["A","C","CLA","CLS","E","G","GL","GLA","GLC","GLE","GLS","S","SLC","SLK"],
    "Mitsubishi": ["ASX","Attrage","Galant","L200","Lancer","Montero","Outlander","Pajero"],
    "Nissan":     ["Altima","Armada","Juke","KICKS","Maxima","Murano","Navara","Pathfinder","Patrol","Sentra","Sunny","Tiida","X-Trail"],
    "Renault":    ["Capture","Duster","Fluence","Koleos","Logan","Megane","Symbol"],
    "Toyota":     ["4Runner","Aurion","Avalon","Avanza","C-HR","Camry","Coaster","Corolla","Corolla Cross","Crown","FJ Cruiser","Fortuner","Hiace","Hilux","Land Cruiser","Land Cruiser 70","Prado","RAV4","Rush","Sequoia","Yaris"],
    "Volkswagen": ["Golf","Jetta","Passat","Tiguan","Touareg"],
}

st.markdown('<div class="section-label">Brand & Model</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    brand = st.selectbox("Brand", sorted(brand_models.keys()), label_visibility="collapsed")
with col2:
    model_name = st.selectbox("Model", brand_models.get(brand, []), label_visibility="collapsed")

st.markdown('<div class="section-label">Year & Mileage</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    year = st.selectbox("Year", list(range(2024, 1999, -1)), label_visibility="collapsed")
with col4:
    kms = st.number_input("Kilometers", min_value=0, step=5000, value=80000, label_visibility="collapsed")

st.markdown('<div class="section-label">Engine & Fuel</div>', unsafe_allow_html=True)

col5, col6, col7 = st.columns(3)
with col5:
    engine = st.number_input("Engine (L)", min_value=1.0, max_value=8.0, step=0.1, value=2.5, label_visibility="collapsed")
with col6:
    fuel = st.selectbox("Fuel", ["Gas", "Diesel", "Hybrid"], label_visibility="collapsed")
with col7:
    transmission = st.selectbox("Gear", ["Automatic", "Manual"], label_visibility="collapsed")

st.markdown('<div class="section-label">Options</div>', unsafe_allow_html=True)
options = st.selectbox("Options", ["Full", "Standard", "Semi Full"], label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Predict Price"):
    input_data = pd.DataFrame(0, index=[0], columns=columns)

    for col_name, val in [("Year", year), ("Kms_Driven", kms), ("Engine_Size", engine)]:
        if col_name in input_data.columns:
            input_data[col_name] = val

    for col_name in [
        f"Brand_{brand}",
        f"Model_{model_name}",
        f"Fuel_Type_{fuel}",
        f"Transmission_{transmission}",
        f"Options_{options}"
    ]:
        if col_name in input_data.columns:
            input_data[col_name] = 1

    prediction = model.predict(input_data)[0]

    st.markdown(f"""
    <div class="result-card">
        <div class="label">ESTIMATED PRICE</div>
        <div class="price">QAR {prediction:,.0f}</div>
        <div class="sub">{brand} {model_name} · {year} · {kms:,} km</div>
        <div class="accuracy">Model accuracy · R² = 0.89</div>
    </div>
    """, unsafe_allow_html=True)