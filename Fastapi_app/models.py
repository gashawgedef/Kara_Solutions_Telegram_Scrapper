from sqlalchemy import Column, Integer, String, DateTime, Text
from database import Base


class TelegramMessage(Base):
    __tablename__ = "telegram_messages"

    id = Column(Integer, primary_key=True, index=True)
    channel_title = Column(String, index=True)
    channel_username = Column(String, index=True)
    message_id = Column(Integer, unique=True, index=True)
    message = Column(Text)
    message_date = Column(DateTime)
    media_path = Column(String)
    emoji_used = Column(String)
    youtube_links = Column(String)
