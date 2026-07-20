import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

URL_API = "http://localhost:8000"

st.set_page_config(page_title="WiWiss Buchungssystem", layout="wide")
st.title("Betriebswirtschaftliches Buchungssystem")

auswahl = st.sidebar.selectbox("Navigation", ["Übersicht & GuV", "Neue Buchung erfassen"])

def buchungen_laden():
    try:
        antwort = requests.get(f"{URL_API}/buchungen/")
        if antwort.status_code == 200:
            return antwort.json()
    except:
        st.error("Verbindung zum Backend fehlgeschlagen.")
    return []

if auswahl == "Neue Buchung erfassen":
    st.header("Neue Buchung anlegen")
    
    with st.form("buchungs_formular"):
        spalte1, spalte2 = st.columns(2)
        with spalte1:
            datum = st.date_input("Buchungsdatum", date.today())
            typ = st.selectbox("Buchungstyp", ["Einnahme", "Ausgabe"])
            betrag = st.number_input("Betrag in €", min_value=0.01, format="%f")
        with spalte2:
            kategorie = st.text_input("Kategorie (z.B. Miete, Gehalt, Material)")
            beschreibung = st.text_area("Beschreibung (optional)")
        
        absenden = st.form_submit_button("Speichern")
        
        if absenden:
            daten = {
                "datum": str(datum),
                "betrag": betrag,
                "kategorie": kategorie,
                "typ": typ,
                "beschreibung": beschreibung
            }
            antwort = requests.post(f"{URL_API}/buchungen/", json=daten)
            if antwort.status_code == 200:
                st.success("Buchung wurde erfolgreich eingetragen!")
            else:
                st.error("Fehler beim Speichern der Daten.")

elif auswahl == "Übersicht & GuV":
    st.header("Buchungsübersicht & Gewinn- und Verlustrechnung (GuV)")
    eintraege = buchungen_laden()
    
    if eintraege:
        df = pd.DataFrame(eintraege)
        
        einnahmen = df[df["typ"] == "Einnahme"]["betrag"].sum()
        ausgaben = df[df["typ"] == "Ausgabe"]["betrag"].sum()
        ergebnis = einnahmen - ausgaben
        
        s1, s2, s3 = st.columns(3)
        s1.metric("Gesamteinnahmen", f"{einnahmen:.2f} €")
        s2.metric("Gesamtausgaben", f"{ausgaben:.2f} €")
        s3.metric("Betriebsergebnis (GuV)", f"{ergebnis:.2f} €")
        
        st.subheader("Alle Buchungen")
        st.dataframe(df[["datum", "typ", "kategorie", "betrag", "beschreibung"]].set_index("datum"), use_container_width=True)
        
        st.subheader("Grafische Auswertung")
        fig, ax = plt.subplots(figsize=(7, 3.5))
        balken = ax.bar(["Einnahmen", "Ausgaben"], [einnahmen, ausgaben], color=['#2ecc71', '#e74c3c'])
        ax.set_ylabel("Betrag in €")
        ax.bar_label(balken, fmt='%.2f €')
        st.pyplot(fig)
        
    else:
        st.info("Es wurden noch keine Buchungen erfasst.")
#Verbleibendes Ziel für die Vertiefung:
    #Getrennte Übersicht der Einnahmen und Ausgaben einschließlich der Kennzahlen wie Spannweite (max und min), Durchschnittswerte je Transaktionstyp und Zeiträume
    #korrigieren und neu einbringen
