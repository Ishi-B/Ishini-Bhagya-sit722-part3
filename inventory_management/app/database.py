from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "DATABASE_URL', 'postgresql://assessment_part_2_user:QJVGtCXlv9JULkLi34Ou7MCc4b9vcGvl@dpg-cripj5jv2p9s738mbqvg-a.singapore-postgres.render.com/assessment_part_2?sslmode=require" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
