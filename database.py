from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Your PostgreSQL Credentilas
DATABASE_URL = "postgressql://postgres:1234@localhost/Sierra_Leone_Concert"

# create the engine to interact with  the database
engine = create_engine(DATABASE_URL)

# create session
SessionLocal = sessionmaker(autocommit=False , autoflush=False ,bind=engine)

# Base class for models
Base = declarative_base()

# dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield  db
    finally:
        db.close()

