import streamlit as st
import numpy as np
import pandas as pd
import joblib  # ✅ use joblib instead of pickle

# Load the trained model
model = joblib.load("best_model.pkl")  # ✅ this ensures model is correct type

# Title
st.title("🌲 Forest Cover Type Prediction")
st.markdown("---")

# Intro / About Section
st.markdown("""
Welcome to the **Forest Cover Prediction App**!  
This tool is designed to predict the **forest cover type** based on various **topographic and geographic features** of a location.

### 📊 Project Summary
- **Objective:** To assist in identifying the dominant forest cover type in a given area using machine learning.
- **Use Case:** This can support forest management, conservation planning, and ecological studies.
- **Algorithm Used:** Trained and optimized using a **Random Forest Classifier** for high accuracy.

### 📁 Dataset Description
The dataset used in this project contains over 500,000 records with 54 features. These include:
- Elevation, slope, aspect, and hillshade at different times of day
- Distances to hydrology, roads, and fire points
- Soil types (40 encoded types)
- Wilderness area classifications

Each record is labeled with a forest cover type (like Spruce/Fir, Aspen, Lodgepole Pine, etc.) based on field survey data from forest regions in the United States.
""")
st.markdown("---")

st.header("Enter Input Features")

# Inputs for the main numeric features
id_value = st.number_input("ID", min_value=0)
elevation = st.number_input("Elevation", min_value=0)
aspect = st.number_input("Aspect", min_value=0, max_value=360)
slope = st.number_input("Slope", min_value=0)
h_dist_hydro = st.number_input("Horizontal Distance to Hydrology", min_value=0)
v_dist_hydro = st.number_input("Vertical Distance to Hydrology", min_value=0)
h_dist_road = st.number_input("Horizontal Distance to Roadways", min_value=0)
hillshade_9am = st.number_input("Hillshade 9am", min_value=0, max_value=255)
hillshade_noon = st.number_input("Hillshade Noon", min_value=0, max_value=255)
hillshade_3pm = st.number_input("Hillshade 3pm", min_value=0, max_value=255)
h_dist_fire = st.number_input("Horizontal Distance to Fire Points", min_value=0)

# Wilderness area (only one can be 1)
wilderness_area = st.selectbox("Wilderness Area", ["Wilderness_Area1", "Wilderness_Area2", "Wilderness_Area3", "Wilderness_Area4"])
wilderness = [1 if f"Wilderness_Area{i+1}" == wilderness_area else 0 for i in range(4)]

# Soil type (only one can be 1)
soil_type = st.selectbox("Soil Type", [f"Soil_Type{i+1}" for i in range(40)])
soil = [1 if f"Soil_Type{i+1}" == soil_type else 0 for i in range(40)]

# Combine all inputs in proper order (including 'Id')
input_data = [id_value, elevation, aspect, slope,
              h_dist_hydro, v_dist_hydro, h_dist_road,
              hillshade_9am, hillshade_noon, hillshade_3pm,
              h_dist_fire] + wilderness + soil

# Predict button
if st.button("Predict Cover Type"):
    input_df = pd.DataFrame([input_data], columns=[
        'Id', 'Elevation', 'Aspect', 'Slope',
        'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
        'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon',
        'Hillshade_3pm', 'Horizontal_Distance_To_Fire_Points',
        'Wilderness_Area1', 'Wilderness_Area2', 'Wilderness_Area3', 'Wilderness_Area4',
        'Soil_Type1', 'Soil_Type2', 'Soil_Type3', 'Soil_Type4', 'Soil_Type5',
        'Soil_Type6', 'Soil_Type7', 'Soil_Type8', 'Soil_Type9', 'Soil_Type10',
        'Soil_Type11', 'Soil_Type12', 'Soil_Type13', 'Soil_Type14', 'Soil_Type15',
        'Soil_Type16', 'Soil_Type17', 'Soil_Type18', 'Soil_Type19', 'Soil_Type20',
        'Soil_Type21', 'Soil_Type22', 'Soil_Type23', 'Soil_Type24', 'Soil_Type25',
        'Soil_Type26', 'Soil_Type27', 'Soil_Type28', 'Soil_Type29', 'Soil_Type30',
        'Soil_Type31', 'Soil_Type32', 'Soil_Type33', 'Soil_Type34', 'Soil_Type35',
        'Soil_Type36', 'Soil_Type37', 'Soil_Type38', 'Soil_Type39', 'Soil_Type40'
    ])

    prediction = model.predict(input_df)[0]  # ✅ Now this works

    # Map prediction to class name
    cover_classes = {
        1: "Spruce/Fir",
        2: "Lodgepole Pine",
        3: "Ponderosa Pine",
        4: "Cottonwood/Willow",
        5: "Aspen",
        6: "Douglas-fir",
        7: "Krummholz"
    }

    st.success(f"🌲 Predicted Forest Cover Type: {cover_classes[prediction]}")
    st.markdown("✅ Prediction generated using the trained Random Forest model.")