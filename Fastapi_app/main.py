from fastapi import FastAPI, Depends, HTTPException
import schema_models, crud, models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

# Create database tables
models.Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API endpoint to get all messages
@app.get("/messages/", response_model=list[schema_models.TelegramMessage])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, skip=skip, limit=limit)
    return messages


# API endpoint to get a message by ID
@app.get("/messages/{message_id}", response_model=schema_models.TelegramMessage)
def read_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud.get_message(db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message


# API endpoint to insert a new message
@app.post("/messages/", response_model=schema_models.TelegramMessage)
def create_message(
    message: schema_models.TelegramMessageCreate, db: Session = Depends(get_db)
):
    return crud.create_message(db=db, message=message)


# API endpoint to delete a message by ID
@app.delete("/messages/{message_id}", response_model=schema_models.TelegramMessage)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud.delete_message(db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message
