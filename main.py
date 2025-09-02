import datetime
from fastapi import FastAPI, Request, Response, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from config.database import SessionLocal 
from dotenv import load_dotenv
from config.database import engine , SessionLocal
from model.todo_model import Todo
from pydantic import BaseModel
import os

load_dotenv()




app = FastAPI()

# Create Database tables through migration
Todo.metadata.create_all(bind=engine)




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


# Pydata model for Todo validation

class TodoCreate(BaseModel):
    title: str
    description: str = None
    status: bool = False


# create a new todo
@app.post("/todos/create")
async def create_todo(todo: TodoCreate, request: Request ,  db = Depends(DBConnect)):
      
    try:

        if not todo.title:
            raise HTTPException(status_code=400, detail="Title is required.")
        
        # # Check if a todo with the same title already exists
        # existing_todo = db.query(Todo).filter(Todo.title == todo.title).first()
        # if existing_todo:
        #     raise HTTPException(status_code=400, detail="Todo with this title already exists.")
        new_todo = Todo(
            title=todo.title,
            description=todo.description,
            status=todo.status,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
      )
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return Response(content=f"Todo with ID {new_todo.id} created successfully.", status_code=201)
    
    except Exception as e:
        print(f"Error creating todo: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error") from e


# crud operation to get all todos
@app.get("/todos")
async def get_todos(db = Depends(DBConnect)):
    try:
        todos = db.query(Todo).all()
        return todos
    except Exception as e:
        print(f"Error fetching todos: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
    

# crud operation to get a specific todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int, db = Depends(DBConnect)):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo
    except Exception as e:
        print(f"Error fetching todo: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
    
# crud operation to update a specific todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: TodoCreate, db = Depends(DBConnect)):
    try:
        existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if existing_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        # Update the existing todo with new values
        existing_todo.title = todo.title
        existing_todo.description = todo.description
        existing_todo.status = todo.status
        existing_todo.updated_at = datetime.datetime.now()

        db.commit()
        db.refresh(existing_todo)
        return Response(content=f"Todo with ID {existing_todo.id} updated successfully.", status_code=200)

    except Exception as e:
        print(f"Error updating todo: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
    
# crud operation to delete a specific todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db = Depends(DBConnect)):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        db.delete(todo)
        db.commit()
        return Response(content=f"Todo with ID {todo.id} deleted successfully.", status_code=200)

    except Exception as e:
        print(f"Error deleting todo: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error") from e