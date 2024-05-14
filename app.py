import streamlit as st

def calculer_metre_lineaire(hauteur_mur, largeur_mur, largeur_papier, raccord):
    # Calculer le nombre de lés nécessaires pour couvrir la largeur du mur
    nombre_les = largeur_mur / largeur_papier
    
    # Calculer la hauteur nécessaire pour chaque lé, en tenant compte du raccord
    hauteur_les = hauteur_mur + raccord
    
    # Calculer le métrage total nécessaire
    metre_lineaire = nombre_les * hauteur_les
    
    return metre_lineaire


st.write("Hello Team Elitis ☀️!")

hauteur_mur = st.number_input("Entrez la hauteur du mur en mètres", value=0, placeholder="Entrez un nombre...")
# st.write(f"La hauteur du mur est de {hauteur_mur} mètres")

largeur_mur = st.number_input("Entrez la largeur du mur en mètres", value=0, placeholder="Entrez un nombre...")
# st.write(f"La largeur du mur est de {largeur_mur} mètres")

largeur_papier = st.number_input("Entrez la largeur du papier peint en mètres", value=1, placeholder="Entrez un nombre...")
# st.write(f"La largeur du papier peint est de {largeur_papier} mètres")

raccord = st.number_input("Entrez le raccord du papier peint en mètres", value=0, placeholder="Entrez un nombre...")
# st.write(f"Le raccord du papier peint est de {raccord} mètres")

# Calcul du métrage nécessaire
metrage_necessaire = calculer_metre_lineaire(hauteur_mur, largeur_mur, largeur_papier, raccord)

# Affichage du résultat
st.write(f"Le métrage nécessaire est de {metrage_necessaire:.2f} mètres linéaires.")
# st.image('images/elitis_logo.png')