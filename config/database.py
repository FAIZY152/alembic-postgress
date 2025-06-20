from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://agentic-ai_owner:npg_8VyPCJ0tElBL@ep-delicate-violet-a1txqv0e-pooler.ap-southeast-1.aws.neon.tech/agentic-ai?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
