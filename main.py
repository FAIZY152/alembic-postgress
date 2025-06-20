from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.database import SessionLocal 
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


# connect to the database
def DBConnect():
    # Placeholder for database connection logic
    db = SessionLocal()
    try:
        yield db
        # Simulate a successful database connection
        print("Database connected successfully.")
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
    finally:
        db.close()

