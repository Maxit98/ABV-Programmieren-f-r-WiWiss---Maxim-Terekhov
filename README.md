# README für Gruppe 6 im ABV Programmieren für Wiwiss
  
  Gruppenmitglied: 
Maxim Terekhov
  
  Funktion der Anwendungs: 
Bei der Anwendung handelt es sich um ein grundlegendes Betriebswirtschaftliches Buchungssystem in
dem 3 Funktionen eingeplant waren.
  1. Die Erfassung neuer Buchungen mit Datum, Typ (Ein und Ausgabe), Betrag in €, und frei wählbaren Textfeldern für
     Kategorie und eine optionale Beschreibung
  2. Einer Übersicht und GuV die die bisherigen Buchungen nach Buchungszeitpunkt absteigend ausgibt, die Einnahmen, Ausgaben
     und das Ergebnis anzeigt, sowie eine grafische Auswertung der beiden als Balkendiagram anzeigt
  3. (Aus Fehlergründen entfernt) einer als kreativen Erweiterung gedachten getrennten Ein- und Ausgabenübersicht welche
     die jeweiligen Spannweiten der Buchungstypen, sowie ihre Deskriptiven Statistiken wie den Durchschnitt und Medien
     anzeigt. #Aufgrund der technischen und zeitlichen Hürden wurde diese aus dem zum 12.07. eingesandten Projekt gestrichen
  
  Kurze Beschreibung des Projektaufbaus:
Das Projekt besteht aus dem für Nutzung der anwendung genutzten Frontend app.py welches Streamlit nutzt, sowie dem für die
übrigen Funktionen wie definierung der Klassen, sowie der Bearbeitung und Speicherung der Objekte/Buchungen genutzten backend
main.py
  
  Kreative Erweiterung:
Mit vorläufigen Verwurf der getrennten Ein- und Ausgabenübersicht verbleibt als kreative Erweiterung leider lediglich die
Datenvisualisierung der Einnahmen und Ausgaben in Form der Grafischen Auswertung im Bereich "Übersicht & GuB".
  
  Anleitung zum Lokalen Start der Anwendung:
Zum Start der Anwendung via VSCode wurden lokal folgende Schritte befolgt:
    - Öffnen zweier Python Terminals mit der Version 3.14.6, sowie den Installierten Paketen zur Ausführung der Anwendungen
    - Öffnen des backends via cd {Dateipfad mit dem git Ordner der das Backend enthält}
    - Start via uv run uvicorn backend.main:app --reload
    - Öffnen des frontends via cd {Dateipfad mit demselben git Ordner der das Frontend enthält}
    - Automatischer Start der Anwendung durch den Code des frontends in http://localhost:8501/

  Dokumentation der KI-Nutzung:
Für die Einführung in die Grundlegende Nutzung des neuen Programms VSCode statt wie bisher jupyterlab, die Grundlegenden Strukturen
eines Funktionsfähigen Frontend und Backend, sowie die ersten technischen Ausführungen der Anwendungen wurde Google Gemini 3.1 
Pro intensiv verwendet.

Diese README wurde nicht mit KI erstellt
Der Ordner .venv wurde aufgrund der Beschränkung für die Übertragung ins Repo via GitHub aus dem Repo entfernt und in die Email mit dem Quelllink als Anhang eingefügt.
