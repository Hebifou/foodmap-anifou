import streamlit as st

st.set_page_config(layout="wide", page_title="Foodmap")
st.markdown("<h1 style='text-align: center;'>Foodmap – Wirkung von Lebensmitteln im Körper</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Lebensmittel")
    item = st.radio("Wähle ein Lebensmittel", ["Apfel", "Datteln", "Linsen", "Leinöl"])

if item == "Apfel":
    st.image("assets/OKY6FW0.jpg", caption="Wirkung auf: Haut, Gehirn, Verdauung", use_column_width=True)
    st.markdown("**Apfel:** Reich an Ballaststoffen und Antioxidantien – gut für Darm, Haut & Gehirn.\
                 Empfohlene Menge: 1-2 Stück pro Tag.")
elif item == "Datteln":
    st.image("assets/body.png", caption="Wirkung auf: Energie, Verdauung, Nerven", use_column_width=True)
    st.markdown("**Datteln:** Natürliche Energiequelle, liefern Kalium & Ballaststoffe.\
                 Empfohlene Menge: 3–5 Stück pro Tag.")
elif item == "Linsen":
    st.image("assets/body.png", caption="Wirkung auf: Muskeln, Blutbildung", use_column_width=True)
    st.markdown("**Linsen:** Proteinreich, eisenhaltig – unterstützt Muskelaufbau & Blutbildung.")
elif item == "Leinöl":
    st.image("assets/body.png", caption="Wirkung auf: Entzündungen, Gehirn, Haut", use_column_width=True)
    st.markdown("**Leinöl:** Reich an Omega-3 – gut für Haut, Hirn & Zellschutz.\
                 1 TL täglich empfohlen (nicht erhitzen).")
