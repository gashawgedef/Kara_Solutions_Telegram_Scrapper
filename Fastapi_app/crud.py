from sqlalchemy.orm import Session
import models, schema_models


def get_message(db: Session, message_id: int):
    return (
        db.query(models.TelegramMessage)
        .filter(models.TelegramMessage.message_id == message_id)
        .first()
    )


def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TelegramMessage).offset(skip).limit(limit).all()


def create_message(db: Session, message: schema_models.TelegramMessageCreate):
    db_message = models.TelegramMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def delete_message(db: Session, message_id: int):
    db_message = (
        db.query(models.TelegramMessage)
        .filter(models.TelegramMessage.message_id == message_id)
        .first()
    )
    if db_message:
        db.delete(db_message)
        db.commit()
        return db_message
    return None
