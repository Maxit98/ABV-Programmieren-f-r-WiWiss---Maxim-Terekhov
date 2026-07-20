from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from datetime import date
from typing import List

DB_URL = "sqlite:///./buchungen.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Buchungen(Base):
    __tablename__ = "buchungen"
    id = Column(Integer, primary_key=True, index=True)
    datum = Column(Date, index=True)
    betrag = Column(Float)
    kategorie = Column(String)
    typ = Column(String)
    beschreibung = Column(String)

Base.metadata.create_all(bind=engine)

class Eingabe(BaseModel):
    datum: date
    betrag: float = Field(..., gt=0)
    kategorie: str
    typ: str = Field(..., pattern="^(Einnahme|Ausgabe)$")
    beschreibung: str

class Ausgabe(Eingabe):
    id: int
    class Config:
        from_attributes = True

app = FastAPI(title="Buchungssystem API")

def gib_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/buchungen/", response_model=Ausgabe)
def buchung_anlegen(buchung_daten: Eingabe, db: Session = Depends(gib_db)):
    neue_buchung = Buchungen(**buchung_daten.model_dump())
    db.add(neue_buchung)
    db.commit()
    db.refresh(neue_buchung)
    return neue_buchung

@app.get("/buchungen/", response_model=List[Ausgabe])
def liste_buchungen(db: Session = Depends(gib_db)):
    return db.query(Buchungen).order_by(Buchungen.datum.desc()).all()

#Verbleibendes Ziel für die Vertiefung:
    #Getrennte Übersicht der Einnahmen und Ausgaben einschließlich der Kennzahlen wie Spannweite (max und min), Durchschnittswerte je Transaktionstyp und Zeiträume
    #korrigieren und neu einbringen
