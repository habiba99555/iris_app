import streamlit as st
import requests

# Fonction pour envoyer les données à l'API
def send_data_to_api(data):
    response = requests.post("http://127.0.0.1:5000/predict", json=data)
    return response.json()


st.markdown("<h1 style='text-align: center;'>TYPE DE FLEUR </h1> ", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    
    sepal_length = st.slider("Longueur du sépal", 0.0, 20.0, value=0.0, step=0.1)

with col2:
    sepal_width = st.slider("Largeur du sépal", 0.0, 20.0, value=0.0, step=0.1)

col3, col4 = st.columns(2)

with col3:
    petal_length = st.slider("Longueur du pétale", 0.0, 20.0, value=0.0, step=0.1)

with col4:
    petal_width = st.slider("Largeur du pétale", 0.0, 20.0, value=0.0, step=0.1)

# Bouton pour envoyer les données à l'API
if st.button("VOIR TYPE FLEUR...", help="Cliquez pour envoyer les données", type="primary"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    
    # Envoie des données à l'API
    response = send_data_to_api(data)
    
    # Afficher la réponse de l'API
    st.write("<p style='font-size: 30px; font-weight: bold;'>Votre fleur est : <span style='color: #000000;'>", response , "</span></p>", unsafe_allow_html=True)


