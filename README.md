# 🌲 Forest Cover Type Prediction

This project is a machine learning application that predicts the forest cover type from cartographic variables. It uses a trained model and a Streamlit web app to make predictions based on user input.

---

## 🚀 Features

- Predicts forest cover type using 54 features including topographical and soil data.
- Interactive Streamlit web interface.
- Trained using a high-accuracy machine learning model.
- Ready for deployment on Streamlit Cloud.

---

## 📁 Project Structure

| File/Folder                        | Description                                  |
| ---------------------------------- | -------------------------------------------- |
| `app.py`                           | Streamlit app for prediction                 |
| `best_model.pkl`                   | Saved trained model                          |
| `dataset.csv`                      | Dataset used for training                    |
| `forestCover.ipynb`                | Jupyter notebook for training and evaluation |
| `requirements.txt`                 | All required Python packages                 |
| `Forest Cover Type Prediction.pdf` | Project report                               |
| `.venv/`                           | Local virtual environment (ignored in Git)   |

## 🧠 Model Details

- **Model used**: Random Forest Classifier (or as trained in notebook)
- **Accuracy**: ~86%
- **Input features**:
  - Elevation, Aspect, Slope
  - Hydrology and Roadway Distances
  - Hillshade values (9am, Noon, 3pm)
  - Wilderness Area (One-hot)
  - Soil Type (One-hot)
- **Target Variable**: Forest Cover Type (7 classes)

---

## 🛠️ Setup Instructions

### Clone the repo

```bash
git clone https://github.com/your-username/forest_cover_prediction.git
cd forest_cover_prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app locally

```bash
streamlit run app.py
```
