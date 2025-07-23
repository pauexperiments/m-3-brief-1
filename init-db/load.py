import sys
import os
import pandas as pd
from sqlalchemy.orm import Session
from datetime import datetime


CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', 'src'))
print(f"Current directory: {CURRENT_DIR}")
print(f"Source directory: {SRC_DIR}")

# add src directory to sys.path
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


from database import SessionLocal, db_create
import models


def load_data(csv_path: str):

    model_cvs_mapping = {
        "first_name": "prenom",
        "last_name": "nom",
        "age": "age",
        "height_cm": "taille",
        "weight_kg": "poids",
        "gender": "sexe",
        "sport_license": "sport_licence",
        "education_level": "niveau_etude",
        "region": "region",
        "smoker": "smoker",
        "is_french_citizen": "nationalité_francaise",
        "estimated_monthly_income": "revenu_estime_mois",
        "marital_status": "situation_familiale",
        "credit_history": "historique_credits",
        "personal_risk_level": "risque_personnel",
        "account_creation_date": "date_creation_compte",
        "credit_score": "score_credit",
        "monthly_rent": "loyer_mensuel",
        "requested_loan_amount": "montant_pret",
        "child_count": "nb_enfants",
        "social_family_quotient": "quotient_caf"
    }



    df = pd.read_csv(csv_path)
    db: Session = SessionLocal()

    try:
        for index, row in df.iterrows():
            record = db.query(models.BorrowerProfile).filter_by(id=index+1).first()
            for col in ["child_count", "social_family_quotient"]:
                setattr(record, col, row[model_cvs_mapping[col]])
                
        db.commit()
        print("✅ Importation terminée.")
    except Exception as e:
        db.rollback()
        print("❌ Erreur :", e)
    finally:
        db.close()

if __name__ == "__main__":
    db_create()
    load_data(os.path.join(CURRENT_DIR, "data.csv"))

