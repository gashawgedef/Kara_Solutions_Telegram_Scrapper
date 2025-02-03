from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class TelegramData(Base):
    __tablename__ = "telegram_data"
    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String)
    message = Column(String)
    date = Column(DateTime)