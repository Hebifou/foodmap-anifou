import streamlit as st

st.set_page_config(layout="wide", page_title="Foodmap")

# ----------------------------
# Datenstruktur mit Kategorien
# ----------------------------
lebensmittel_daten = {
    "Früchte": {
        "Apfel": {
            "wirkung": "Reich an Ballaststoffen und Antioxidantien – gut für Darm, Haut & Gehirn.",
            "menge": "1–2 Stück pro Tag.",
            "quelle": "DGE",
            "bereiche": {
                "Darm": "Fördert die Verdauung und unterstützt das Mikrobiom.",
                "Haut": "Antioxidantien helfen beim Zellschutz.",
                "Gehirn": "Liefert Energie für Konzentration und mentale Leistung."
            }
        }
    },
    "Hülsenfrüchte": {
        "Linsen": {
            "wirkung": "Reich an Eiweiß und Eisen – wichtig für Blutbildung und Energie.",
            "menge": "1 Portion (ca. 150g) pro Tag.",
            "quelle": "DGE",
            "bereiche": {
                "Muskeln": "Proteinreich – unterstützt den Muskelaufbau.",
                "Blut": "Enthält Eisen – fördert die Blutbildung.",
                "Nerven": "Hilft beim Energiestoffwechsel und der Nervengesundheit."
            }
        }
    }
}

# ----------------------------
# Sidebar – Auswahl & Infos
# ----------------------------
with st.sidebar:
    st.markdown("### Wirkung nach Körperregion")

    st.markdown("### Lebensmittel-Auswahl")
    selected_kategorie = st.selectbox("Kategorie", list(lebensmittel_daten.keys()))
    selected_item = st.selectbox("Lebensmittel", list(lebensmittel_daten[selected_kategorie].keys()))

    daten = lebensmittel_daten[selected_kategorie][selected_item]

    st.markdown("---")
    st.markdown(f"###{selected_item}")
    st.markdown(f"**Wirkung:** {daten['wirkung']}")
    st.markdown(f"**Menge:** {daten['menge']}")
    st.markdown(f"**Quelle:** *{daten['quelle']}*")

    if "bereiche" in daten:
        st.markdown("### Wirkung nach Körperregion")
        for region, beschreibung in daten["bereiche"].items():
            st.markdown(f"🔹 **{region}:** {beschreibung}")

# ----------------------------
# Hauptbereich – Bildanzeige
# ----------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("body.png", width=500, caption=f"Wirkung von {selected_item}")
