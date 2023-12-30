import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Load environment variables from .env
load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")

# Use an f-string to include the value of DB_PASSWORD
DATABASE_URI = f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5432/postgres"

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
