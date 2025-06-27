import streamlit as st

st.set_page_config(layout="wide", page_title="Foodmap")
st.markdown("<h1 style='text-align: center;'>Foodmap – Wirkung von Lebensmitteln im Körper</h1>", unsafe_allow_html=True)

# ----------------------------
# Datenstruktur mit Kategorien
# ----------------------------
lebensmittel_daten = {
    "Früchte": {
        "Apfel": {
            "wirkung": "Reich an Ballaststoffen und Antioxidantien – gut für Darm, Haut & Gehirn.",
            "menge": "1–2 Stück pro Tag.",
            "quelle": "DGE"
        },
        "Kiwi": {
            "wirkung": "Vitamin-C-reich, stärkt das Immunsystem und unterstützt die Verdauung.",
            "menge": "1–2 Stück täglich.",
            "quelle": "Harvard Health Publishing"
        }
    },
    "Hülsenfrüchte": {
        "Kichererbsen": {
            "wirkung": "Proteinreich, fördern Muskelaufbau und sättigen nachhaltig.",
            "menge": "1 Portion (ca. 150g) pro Tag.",
            "quelle": "DGE"
        },
        "Linsen": {
            "wirkung": "Reich an Eiweiß und Eisen – wichtig für Blutbildung und Energie.",
            "menge": "1 Portion (ca. 150g) pro Tag.",
            "quelle": "DGE"
        }
    }
    # Weitere Kategorien folgen...
}

# ----------------------------
# Sidebar für Auswahl
# ----------------------------
with st.sidebar:
    st.markdown("### Lebensmittel-Auswahl")
    selected_kategorie = st.selectbox("Kategorie", list(lebensmittel_daten.keys()))
    selected_item = st.selectbox("Lebensmittel", list(lebensmittel_daten[selected_kategorie].keys()))

daten = lebensmittel_daten[selected_kategorie][selected_item]

# ----------------------------
# Anzeige im Hauptbereich
# ----------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    
    st.image("body.png", width=1000, caption=f"Wirkung von {selected_item}")
    st.markdown(f"### 🥑 {selected_item}")
    st.markdown(f"**Wirkung:** {daten['wirkung']}")
    st.markdown(f"**Empfohlene Menge:** {daten['menge']}")
    st.markdown(f"**Quelle:** *{daten['quelle']}*")
