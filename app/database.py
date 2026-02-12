import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL= 'postgresql://hrms_db_k7qq_user:l9zuCz5cHrTaYjNBneNCtjXl4YDN5kh8@dpg-d66q3475r7bs739d37gg-a:5432/hrms_db_k7qq'
#DATABASE_URL= 'postgresql://postgres:password@localhost:5432/hrms'

#os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
