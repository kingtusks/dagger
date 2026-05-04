from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from decouple import config

engine = create_engine(config("POSTGRES_URL"))
sessionDB = sessionmaker(autoflush=False, bind=engine)