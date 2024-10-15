import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV")

if(ENV == "development"):
    SQLALCHEMY_DATABASE_URL = os.getenv("DEV_DATABASE_URL")
else: 
    SQLALCHEMY_DATABASE_URL = os.getenv("PROD_DATABASE_URL")


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()